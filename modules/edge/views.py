import csv

from django.shortcuts import render
from modules.cnmb import views as views_cnmb
from modules.cnmb.forms import FileUploadCnmbForm
from modules.umls import views as views_umls
from modules.umls.forms import FileUploadUmlsForm


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
    search = data['search'] if data['search'] is not None else ''
    database_selected = "UMLS"
    form = FileUploadUmlsForm(request.POST, request.FILES)
    return render(request, 'base.html', locals())


def process_cnmb(request):
    options_database = get_databases()
    data = views_cnmb.process(request)
    object_list = data['object_list']
    search = data['search']
    search_by_csv = data['search_by_csv']
    database_selected = "CNMB"
    return render(request, 'base.html', locals())


def get_databases():
    return ['UMLS', 'CNMB', ]


def upload_csv_umls(request):
    if request.method == 'POST':
        form = FileUploadUmlsForm(request.POST, request.FILES)
        if form.is_valid():
            is_valid=True
            error = None
            file = request.FILES['file']
            index = file.name.find('.')
            format = file.name[index:]
            if format == '.csv':
                handle_uploaded_file(request.FILES['file'], 'codes_umls.csv')
            else:
                error = 'El formato del archivo que intenta subir es incorrecto.'
        else:
            is_valid = False
    else:
        form = FileUploadUmlsForm()

    database_selected = 'UMLS'

    return render(request, 'upload_umls_successfull.html', locals())


def upload_csv_cnmb(request):
    if request.method == 'POST':
        form = FileUploadCnmbForm(request.POST, request.FILES)
        error = None
        if form.is_valid():
            is_valid=True
            file = request.FILES['file']
            index = file.name.find('.')
            format = file.name[index:]
            if format == '.csv':
                handle_uploaded_file(request.FILES['file'], 'codes_cnmb.csv')
            else:
                error = 'El formato del archivo que intenta subir es incorrecto.'
        else:
            is_valid = False
    else:
        form = FileUploadCnmbForm()

    database_selected = 'CNMB'

    return render(request, 'upload_umls_successfull.html', locals())


def handle_uploaded_file(f, file_name):
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
