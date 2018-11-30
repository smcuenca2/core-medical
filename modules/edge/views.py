from django.shortcuts import render
from modules.umls import views as views_umls


def index(request):
    options_database = get_databases()
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


def get_databases():
    return ['UMLS', 'CNMB', ]
