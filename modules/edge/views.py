from django.shortcuts import render
from modules.umls import views as views_umls
from modules.cnmb import views as views_cnmb


def index(request):
    options_database = get_databases()
    database_selected = "UMLS"
    option_relations = views_umls.get_relations()
    return render(request, 'base.html', locals())


def process(request):
    """
    Permite renderizar la página inicial
    :param request:
    :return:
    """
    options_database = get_databases()
    database_selected = request.GET.get('database-selected')
    option_relations = []
    cnmb_levels = []

    if database_selected == 'UMLS':
        option_relations = views_umls.get_relations()

    return render(request, 'base.html', locals())


def process_umls(request):
    """
    Permite llamar al metodo procesar datos umls contenidos en la app uml.
    :param request:
    :return:
    """
    options_database = get_databases()
    data = views_umls.process(request)
    object_list = data['object_list']
    relation_selected = data['relation_selected']
    option_relations = data['option_relations']
    search = data['search']
    database_selected = "UMLS"
    return render(request, 'base.html', locals())


def process_cnmb(request):
    options_database = get_databases()
    data = views_cnmb.process(request)
    object_list = data['object_list']
    search = data['search']
    database_selected = "CNMB"
    return render(request, 'base.html', locals())


def get_databases():
    return ['UMLS', 'CNMB', ]
