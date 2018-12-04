import csv

from django.conf import settings
from django.core.paginator import Paginator
from modules.umls.utils.dto import Relation, ConceptDTO
from pymedtermino.umls import *


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

    codes_list=read_codes()

    if search is not None and search != "":
        umls_cui = UMLS_CUI(search)
        list_umls_cui.append(umls_cui)
    else:
        for code_umls in codes_list:
            umls_cui = UMLS_CUI(code_umls)
            list_umls_cui.append(umls_cui)

    for umls_cui in list_umls_cui:
        if relation_selected in umls_cui.relations:
            for relations in getattr(umls_cui, relation_selected):
                if relations.code.upper() in codes_list:
                    concept = ConceptDTO()
                    concept.relation = Relation()
                    concept.code = umls_cui.code
                    concept.term = umls_cui.term
                    concept.original_terminologies = umls_cui.original_terminologies
                    concept.relation.term = relations.term
                    concept.terminology = umls_cui.terminology.name
                    concept.relation.code = relations.code
                    concepts.append(concept)

    paginator = Paginator(concepts, PAGINATOR_NUMBER_ITEMS)
    page = request.GET.get('page')
    object_list = paginator.get_page(page)

    return {'object_list': object_list, 'relation_selected': relation_selected,
            'option_relations': option_relations, 'search': search}


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
            'has_contraindicated_drug', 'may_be_diagnosed_by', 'may_treat']


def read_codes():
    """
    Este método permite almacenar los codigos umls que estań en el archivo csv
    :return:
    """
    codes_list = []

    with open('codes_umls.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')

        for row in csv_reader:
            codes_list.append(row['CUI'].upper())
    return codes_list
