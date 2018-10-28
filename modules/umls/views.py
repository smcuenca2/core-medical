import csv

from django.conf import settings
from modules.umls.utils.dto import SicknessTreatDTO
from pymedtermino.umls import *


def process_codes_from_file(file=None):
    DATABASE_CONFIG = getattr(settings, "DATABASES", None)
    DATABASE_HOST = DATABASE_CONFIG['default']['HOST']
    DATABASE_USER = DATABASE_CONFIG['default']['USER']
    DATABASE_PASSWORD = DATABASE_CONFIG['default']['PASSWORD']
    DATABASE_NAME = DATABASE_CONFIG['default']['NAME']

    connect_to_umls_db(DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD,
                       DATABASE_NAME, encoding="latin1")

    list_umls_cui = []

    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')

        for row in csv_reader:
            umls_cui = UMLS_CUI(row['CUI'])
            list_umls_cui.append(umls_cui)

    for umls_cui in list_umls_cui:
        if 'may_be_treated_by' in umls_cui.relations:
            for relations in umls_cui.may_be_treated_by:
                sicknessTreatDTO = SicknessTreatDTO()
                sicknessTreatDTO.code = umls_cui.code
                sicknessTreatDTO.term = umls_cui.term
                sicknessTreatDTO.original_terminologies = umls_cui.original_terminologies
                sicknessTreatDTO.term_rel = relations.term
                sicknessTreatDTO.terminology = umls_cui.terminology.name
