import csv

from django.shortcuts import render
from pymedtermino import *
from pymedtermino.umls import *
from django.conf import settings


# Create your views here.
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
            code = row['CUI']

            list_umls_cui.append(UMLS_CUI[code])

    for umls_cui in list_umls_cui:
        print (umls_cui.code)
