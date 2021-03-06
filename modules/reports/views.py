import csv

from django.db.models import Q
from django.http import HttpResponse
from django.template import Context, loader
from django.template.loader import get_template
from pymedtermino.umls import *
from weasyprint import HTML

from modules.cnmb.models import Physic
from modules.cnmb.utils.dto import CnmbDto
from modules.umls.utils.dto import ConceptDTO, DataUmls, DataCsv, Relation
from modules.umls.views import connect_to_umls


def generate_data_cnmb():
    query_physics = Physic.objects.using('cnmb').order_by('name')
    physic_list = []
    codes = read_codes_cnmb()
    list_by_csv = []
    cnmb_list = []
    for code in codes:
        list_by_csv = query_physics.filter(
            Q(group__code=code) | Q(name__istartswith=code) | Q(
                group__parent__code=code) | Q(
                group__parent__parent__code=code) | Q(
                group__parent__parent__parent__code=code) | Q(
                group__parent__parent__parent__parent__code=code) | Q(
                group__parent__parent__parent__parent__parent__code=code) | Q(
                group__parent__parent__parent__parent__parent__code=code)).all()
        physic_list.extend(list_by_csv)

    for physic in physic_list:
        cnmb_dto = CnmbDto()
        cnmb_dto.physic = physic
        cnmb_dto.care_level_one = physic.cares.filter(level='I').first()
        cnmb_dto.care_level_second = physic.cares.filter(level='II').first()
        cnmb_dto.care_level_third = physic.cares.filter(level='III').first()
        cnmb_list.append(cnmb_dto)
    return cnmb_list


def generate_report_cnmb(request):
    print (request.GET)
    if 'button-print-pdf' in request.GET.keys():
        return report_cnmb_pdf(request)
    else:
        return report_cnmb_txt(request)


def report_cnmb_pdf(request):
    cnmb_list = generate_data_cnmb()
    html_template = get_template('search_cnmb.html').render(
        {'title': 'Resultados de Búsqueda', 'object_list': cnmb_list})
    pdf_file = HTML(string=html_template).write_pdf()
    http_response = HttpResponse(pdf_file, content_type='application/pdf')
    return http_response


def generate_data_umls():
    data_csv_list = read_codes_umls()
    connect_to_umls()
    list_umls_cui = []
    concepts = []
    for data_csv in data_csv_list:
        umls_cui = UMLS_CUI(data_csv.code)
        umls = DataUmls()
        umls.umls = umls_cui
        umls.term = data_csv.name
        list_umls_cui.append(umls)

    codes_list = [data.code for data in data_csv_list]
    for umls_cui in list_umls_cui:
        for el in ['may_be_treated_by', 'may_be_prevented_by',
                   'may_be_diagnosed_by',
                   'may_treat', 'may_prevent', 'may_diagnose']:
            if (el in umls_cui.umls.relations):
                for relations in getattr(umls_cui.umls, el):
                    if relations.code.upper() in codes_list:
                        concept = ConceptDTO()
                        concept.relation = Relation()
                        concept.code = umls_cui.umls.code
                        concept.term = umls_cui.umls.term
                        concept.original_terminologies = ' '.join(
                            list(umls_cui.umls.original_terminologies))
                        concept.relation.term = relations.term
                        concept.terminology = umls_cui.umls.terminology.name
                        concept.term_umls = umls_cui.term
                        concept.relation_selected = el
                        concept.relation.code = relations.code
                        concepts.append(concept)
    return concepts


def generate_report_umls(request):
    if 'button-print-pdf' in request.GET.keys():
        return report_umls_pdf(request)
    else:
        return report_umls_txt(request)


def report_umls_pdf(request):
    concepts = generate_data_umls()
    html_template = get_template('search_umls.html')
    html = html_template.render(
        {'title': 'Resultados de Búsqueda', 'object_list': concepts})
    pdf_file = HTML(string=html).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="results.pdf"'

    return response


def read_codes_umls():
    """
    Este método permite almacenar los codigos umls que estań en el archivo csv
    :return:
    """

    codes_list = []
    with open('codes_umls.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')

        for row in csv_reader:
            if 'CUI' in row and 'NAME' in row:
                data = DataCsv()
                data.code = row['CUI'].upper()
                data.name = row['NAME']
                codes_list.append(data)
    return codes_list


def read_codes_cnmb():
    """
    Este método permite almacenar los codigos de los medicamentos cnmb que estań en el archivo csv
    :return:
    """
    codes_list = []
    with open('codes_cnmb.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')

        for row in csv_reader:
            if 'code' in row:
                codes_list.append(row['code'])
    return codes_list


def report_umls_txt(request):
    concepts = generate_data_umls()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="results_umls.txt"'
    writer = csv.writer(response)
    writer.writerow(
        ['Codigo', 'TerminoUml', 'Termino', 'Relacion', 'CodigoRelacion',
         'TerminoRelacion', 'Terminologia'])
    for concept in concepts:
        writer.writerow(
            [concept.code, concept.term_umls, concept.term,
             concept.relation_selected, concept.relation.code,
             concept.relation.term, concept.original_terminologies])
    return response


def report_cnmb_txt(request):
    cnmb_list = generate_data_cnmb()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="results_cnmb.txt"'
    writer = csv.writer(response)
    writer.writerow(
        ['Codigo', 'Descripcion', 'FormaFarmaceutica', 'Concentracion',
         'NivelPrescripcion',
         'NivelAtencionI', 'NivelAtencionII', 'NivelAtencionIII', '2N',
         'Descripcion2N', '1N', 'Descripcion1N'])
    for cnmb in cnmb_list:
        one_level = 'Si' if cnmb.care_level_one is not None else 'No'
        sec_level = 'Si' if cnmb.care_level_second is not None else 'No'
        third_level = 'Si' if cnmb.care_level_third is not None else 'No'
        writer.writerow(
            [cnmb.physic.group.code, cnmb.physic.name,
             cnmb.physic.pharmaceuticalform,
             '',
             cnmb.physic.prescription_level.level,
             one_level, sec_level, third_level,
             cnmb.physic.group.parent.parent.parent.code,
             cnmb.physic.group.parent.parent.parent.name,
             cnmb.physic.group.parent.parent.parent.parent.code if cnmb.physic.group.parent.parent.parent.parent is not None else '',
             cnmb.physic.group.parent.parent.parent.parent.name if cnmb.physic.group.parent.parent.parent.parent is not None else ''])
    return response
