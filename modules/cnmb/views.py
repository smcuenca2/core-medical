# Create your views here.
import csv
import datetime
import logging
from builtins import Exception

from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from modules.cnmb.models import Physic, Concentration, \
    PrescriptionLevel, RouteAdministration, GroupATC, CareLevel
from modules.cnmb.utils.dto import CnmbDto


def get_database():
    databases = list(getattr(settings, "DATABASES", None))
    return databases


def import_data():
    database = get_database()[1]
    prescription_level_values = {
        '': 'Médico general y/o especialista en cualquier nivel de atención',
        'P': 'Sujeta a la definición de protocolos',
        'E': 'Médico especialista',
        'H': 'A nivel hospitalario y en Unidades Médicas que dispongan de Hospital del día para realizar cirugía ambulatoria.',
        'He': 'Médico especialista en un hospital u hospitalización'}

    care_level_values = {
        'I': 'Puestos de salud, Consultorio General y Centros de Salud A,B y C',
        'II': 'Hospitalario: Hospital básico y Hospital General; Ambulatorio Consultorio de especialidad (es)Clínicas quirúrgicas, Centro de Especialidades , Hospital del día.',
        'III': 'Hospital especializado y hospital de especialidades; Ambulatorio-Centros Especializados'}

    pharmaceuticalform_values = {'Sólido oral': 'SO',
                                 'Líquido para inhalación': 'LI',
                                 'Líquido parenteral': 'LP',
                                 'Líquido oral': 'LO', 'Líquido cutáneo': 'LC',
                                 'Líquido oftálmico': 'LOF',
                                 'Líquido parenteral o sólido parenteral': 'LPS',
                                 'Semisólido cutáneo': 'SC',
                                 'Semisólido oftálmico': 'SOF',
                                 'Semisólido vaginal': 'SV',
                                 'Sólido parenteral': 'SPA'}

    with open('cnmb.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            try:
                # concat level whit pharmaceuticalform for code
                logging.info('starting...')
                code_physic = '%s%s%s' % (row['code_level5'].strip(),
                                          "-" + pharmaceuticalform_values[
                                              row['pharmaceuticalform']] if row[
                                                                                'pharmaceuticalform'] in pharmaceuticalform_values else 'None',
                                          '-' + row['concentration'].replace(
                                              ' ', '') if row[
                                                              'concentration'] != '' else 'None')
                physic = Physic.objects.using(database).filter(
                    code=code_physic).first()
                # create physic.
                if physic is None:
                    physic = Physic()
                    physic.code = code_physic
                    physic.name = row['name_physic']
                    physic.pharmaceuticalform = row['pharmaceuticalform']

                    # save measure
                    if row['concentration'] != '':
                        # create concentration
                        concentration = Concentration()
                        concentration.amount = 0.0
                        concentration.name = row['concentration']
                        concentration.update_at = datetime.datetime.now()
                        concentration.save(using=database)
                        logging.info('concentration saved')
                        physic.concentration_id = concentration.id

                    # group level 1
                    group_level_first = GroupATC.objects.using(
                        database).filter(
                        code=row['code_level1'].strip()).first()
                    if group_level_first is None:
                        group_level_first = GroupATC()
                        group_level_first.code = code = row[
                            'code_level1'].strip()
                        group_level_first.name = row['name_level1']
                        group_level_first.level = 1
                        group_level_first.update_at = datetime.datetime.now()
                        group_level_first.save(using=database)

                    # group level 2
                    group_level_second = GroupATC.objects.using(
                        database).filter(
                        code=row['code_level2'].strip()).first()
                    if group_level_second is None:
                        group_level_second = GroupATC()
                        group_level_second.code = code = row[
                            'code_level2'].strip()
                        group_level_second.name = row['name_level2']
                        group_level_second.level = 2
                        group_level_second.parent_id = group_level_first.id
                        group_level_second.update_at = datetime.datetime.now()
                        group_level_second.save(using=database)

                    # group level 3
                    group_level_third = GroupATC.objects.using(
                        database).filter(
                        code=row['code_level3'].strip()).first()
                    if group_level_third is None:
                        group_level_third = GroupATC()
                        group_level_third.code = code = row[
                            'code_level3'].strip()
                        group_level_third.name = row['name_level3']
                        group_level_third.level = 3
                        group_level_third.parent_id = group_level_second.id
                        group_level_third.update_at = datetime.datetime.now()
                        group_level_third.save(using=database)

                    # group level 4
                    group_level_four = GroupATC.objects.using(
                        database).filter(
                        code=row['code_level4'].strip()).first()
                    if group_level_four is None:
                        group_level_four = GroupATC()
                        group_level_four.code = code = row[
                            'code_level4'].strip()
                        group_level_four.name = row['name_level4']
                        group_level_four.level = 4
                        group_level_four.parent_id = group_level_third.id
                        group_level_four.update_at = datetime.datetime.now()
                        group_level_four.save(using=database)

                    # group level 5
                    group_level_five = GroupATC.objects.using(
                        database).filter(
                        code=row['code_level5'].strip()).first()
                    if group_level_five is None:
                        group_level_five = GroupATC()
                        group_level_five.code = code = row[
                            'code_level5'].strip()
                        group_level_five.name = row['name_physic']
                        group_level_five.level = 5
                        group_level_five.parent_id = group_level_four.id
                        group_level_five.update_at = datetime.datetime.now()
                        group_level_five.save(using=database)

                    # search level prescription
                    if row['prescription_level'] != "":

                        prescription_level = PrescriptionLevel.objects.using(
                            database).filter(
                            level=row['prescription_level'].strip()).first()

                        if prescription_level is None:
                            prescription_level = PrescriptionLevel()
                            prescription_level.level = row[
                                'prescription_level'].strip()
                            prescription_level.name = \
                                prescription_level_values[
                                    row['prescription_level']] if row[
                                                                      'prescription_level'] in prescription_level_values else ''
                            prescription_level.update_at = datetime.datetime.now()
                            prescription_level.save(using=database)

                    physic.group_id = group_level_five.id
                    physic.update_at = datetime.datetime.now()
                    physic.prescription_level_id = prescription_level.id
                    physic.save(using=database)

                    # search route
                    route = RouteAdministration.objects.using(
                        database).filter(
                        name=row['route'].strip()).first()
                    if route is None:
                        route = RouteAdministration()
                        route.name = row['route'].strip()
                        route.physic_id = physic.id
                        route.update_at = datetime.datetime.now()
                        route.save(using=database)

                    # care level 1
                    care_level1 = CareLevel.objects.using(database).filter(
                        level='I').first()
                    if care_level1 is None:
                        care_level1 = CareLevel()
                        care_level1.level = 'I'
                        care_level1.name = care_level_values[
                            'I'] if 'I' in care_level_values else ''
                        care_level1.update_at = datetime.datetime.now()
                        care_level1.save(using=database)
                    if row['care_level1'] == 'x':
                        care_level1.physics.add(physic)

                    # care level 2
                    care_level2 = CareLevel.objects.using(database).filter(
                        level='II').first()
                    if care_level2 is None:
                        care_level2 = CareLevel()
                        care_level2.level = 'II'
                        care_level2.name = care_level_values[
                            'II'] if 'II' in care_level_values else ''
                        care_level2.update_at = datetime.datetime.now()
                        care_level2.save(using=database)
                    if row['care_level2'] == 'x':
                        care_level2.physics.add(physic)

                    # care level 3
                    care_level3 = CareLevel.objects.using(database).filter(
                        level='III').first()
                    if care_level3 is None:
                        care_level3 = CareLevel()
                        care_level3.level = 'III'
                        care_level3.name = care_level_values[
                            'III'] if 'III' in care_level_values else ''
                        care_level3.update_at = datetime.datetime.now()
                        care_level3.save(using=database)
                    if row['care_level3'] == 'x':
                        care_level3.physics.add(physic)

                    logging.info('row saved successfully')
                else:
                    logging.warning('physic is already.')
            except Exception as e:
                logging.error('row was not saved', e)


def index(request):
    object_list = []
    return render(request, 'index_cnmb.html', locals())


def process(request):
    object_list = []

    search = request.GET.get('search')
    PAGINATOR_NUMBER_ITEMS = getattr(settings, "PAGINATOR_NUMBER_ITEMS",
                                     None)
    database = get_database()[1]

    query_physics = Physic.objects.using(database).order_by('name')

    cnmb_list = []
    physic_list = []

    if search is not None and search != "":
        physic_list = query_physics.filter(
            Q(group__code=search) | Q(name__istartswith=search)).all()
    else:
        physic_list = query_physics.all()

    for physic in physic_list:
        cnmb_dto = CnmbDto()
        cnmb_dto.physic = physic
        cnmb_dto.care_level_one = physic.cares.filter(level='I').first()
        cnmb_dto.care_level_second = physic.cares.filter(level='II').first()
        cnmb_dto.care_level_third = physic.cares.filter(level='III').first()
        cnmb_list.append(cnmb_dto)

    paginator = Paginator(cnmb_list, PAGINATOR_NUMBER_ITEMS)
    page = request.GET.get('page')
    object_list = paginator.get_page(page)
    return render(request, 'index_cnmb.html', locals())
