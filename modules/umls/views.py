import csv

from django.conf import settings
from django.core.paginator import Paginator
from pymedtermino.umls import *

from modules.umls.utils.dto import Relation, ConceptDTO, DataCsv, DataUmls


def process(request):
    """
    Este método permite presentar la relación entre enferemedades y tratamientos
    mediante el uso de un filtro cuyos códigos se encuentran en un archivo csv.
    :param request:
    :return:
    """

    search = request.GET.get('search')
    option_relations = get_relations()
    relation_selected = request.GET.get('relation-selected')
    PAGINATOR_NUMBER_ITEMS = getattr(settings, "PAGINATOR_NUMBER_ITEMS",
                                     None)
    connect_to_umls()
    list_umls_cui = []
    concepts = []

    data_csv_list = read_codes()

    if search is not None and search != "":
        umls_cui = UMLS_CUI(search)
        umls = DataUmls()
        umls.umls = umls_cui
        umls.term = search_term_umls(search)
        list_umls_cui.append(umls)
    else:
        for data_csv in data_csv_list:
            umls_cui = UMLS_CUI(data_csv.code)
            umls = DataUmls()
            umls.umls = umls_cui
            umls.term = data_csv.name
            list_umls_cui.append(umls)

    codes_list = [data.code for data in data_csv_list]

    for umls_cui in list_umls_cui:
        # Si busco por codigo ignoro la relación seleccionada.
        if search is not None and search != "":
            for rel in get_relations():
                if rel in umls_cui.umls.relations:
                    for relations in getattr(umls_cui.umls, rel):
                        if relations.code.upper() in codes_list:
                            buildUmls(concepts, umls_cui, relations)
            continue
        if relation_selected in umls_cui.umls.relations:
            for relations in getattr(umls_cui.umls, relation_selected):
                if relations.code.upper() in codes_list:
                    buildUmls(concepts, umls_cui, relations)

    paginator = Paginator(concepts, PAGINATOR_NUMBER_ITEMS)
    page = request.GET.get('page')
    object_list = paginator.get_page(page)

    return {'object_list': object_list, 'relation_selected': relation_selected,
            'option_relations': option_relations, 'search': search}


def buildUmls(concepts, umls_cui, relations):
    codes_concept = [concept.code for concept in concepts]
    if umls_cui.umls.code not in codes_concept:
        concept = ConceptDTO()
        concept.relation = Relation()
        concept.code = umls_cui.umls.code
        concept.term = umls_cui.umls.term
        concept.original_terminologies = ' '.join(
            list(umls_cui.umls.original_terminologies))
        concept.relation.term = relations.term
        concept.terminology = umls_cui.umls.terminology.name
        concept.term_umls = umls_cui.term
        concept.relation.code = relations.code
        concepts.append(concept)


def connect_to_umls():
    """
    Este método permite conectarse a la base de datos umls.
    :return:
    """
    DATABASE_CONFIG = getattr(settings, "DATABASES", None)
    DATABASE_HOST = DATABASE_CONFIG['default']['HOST']
    DATABASE_USER = DATABASE_CONFIG['default']['USER']
    DATABASE_PASSWORD = DATABASE_CONFIG['default']['PASSWORD']
    DATABASE_NAME = DATABASE_CONFIG['default']['NAME']
    connect_to_umls_db(DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD,
                       DATABASE_NAME, encoding="latin1")


def get_relations():
    return ['may_be_treated_by', 'may_be_prevented_by', 'may_be_diagnosed_by',
            'may_treat', 'may_prevent', 'may_diagnose']


def search_term_umls(code):
    result = ''
    with open('codes_umls.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            if code.upper() == row['CUI'].upper():
                result = row['NAME']
    return result


def read_codes():
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
