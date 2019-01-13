import csv

from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML

from modules.cnmb.models import Physic


def report_search_cnmb(request):
    query_physics = Physic.objects.using('cnmb').order_by('name')
    physic_list = []
    codes = read_codes()
    list_by_csv = []
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

    html_template = get_template('search_cnmb.html').render(
        {'title': 'Ejemplo', 'list': list})
    pdf_file = HTML(string=html_template).write_pdf()
    http_response = HttpResponse(pdf_file, content_type='application/pdf')
    return http_response


def read_codes():
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
