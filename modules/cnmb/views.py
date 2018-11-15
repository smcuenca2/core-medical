# Create your views here.
import csv
import logging
from decimal import Decimal

from django.db import IntegrityError, transaction
from modules.cnmb.models import Physic, Measure, Concentration, \
    PrescriptionLevel, RouteAdministration, GroupATC, CareLevel


def import_data():
    prescrption_level_values = {
        '': 'Médico general y/o especialista en cualquier nivel de atención',
        'P': 'Sujeta a la definición de protocolos',
        'E': 'Médico especialista',
        'H': 'A nivel hospitalario y en Unidades Médicas que dispongan de Hospital del día para realizar cirugía ambulatoria.',
        'He': 'Médico especialista en un hospital u hospitalización'}
    care_level_values = {
        'I': 'Puestos de salud, Consultorio General y Centros de Salud A,B y C',
        'II': 'Hospitalario: Hospital básico y Hospital General; Ambulatorio Consultorio de especialidad (es)Clínicas quirúrgicas, Centro de Especialidades , Hospital del día.',
        'III': 'Hospital especializado y hospital de especialidades; Ambulatorio-Centros Especializados'}
    with open('cnmb.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            try:
                with transaction.atomic():
                    physic = Physic.objects.filter(
                        code=row['code_physic']).first()
                    # create physic.
                    if physic is None:
                        physic = Physic()
                        physic.code = row['code_physic']
                        physic.name = row['name_physic']
                        physic.pharmaceuticalform = row['pharmaceuticalform']

                        # search concentration.
                        concentration_split = []
                        if row['concentration'] != '':
                            concentration_split = row['concentration'].split(
                                ' ')

                        # save measure
                        if len(concentration_split) > 1:
                            measure_code = concentration_split[1]
                            measure = Measure.objects.filter(
                                code=measure_code).first()
                            if measure is None:
                                # create measure
                                measure = Measure()
                                measure.code = measure_code
                                measure.name = measure_code
                                measure.save()
                            # create concentration
                            concentration = Concentration()
                            concentration.measure_id = measure.id
                            concentration.amount = Decimal(
                                concentration_split[0])
                            concentration.name = concentration_str
                            concentration.save()

                        physic.concentration_id = concentration.id

                        # group level 1
                        group_level_first = GroupATC.objects.filter(
                            code=row['code_level1']).first()
                        if group_level_first is None:
                            group_level_first.code = code = row['code_level1']
                            group_level_first.name = row['name_level1']
                            group_level_first.level = 1
                            group_level_first.save()

                        # group level 2
                        group_level_second = GroupATC.objects.filter(
                            code=row['code_level2']).first()
                        if group_level_second is None:
                            group_level_second.code = code = row['code_level2']
                            group_level_second.name = row['name_level2']
                            group_level_second.level = 2
                            group_level_second.parent_id = group_level_first.id
                            group_level_second.save()

                        # group level 3
                        group_level_third = GroupATC.objects.filter(
                            code=row['code_level3']).first()
                        if group_level_third is None:
                            group_level_third.code = code = row['code_level3']
                            group_level_third.name = row['name_level3']
                            group_level_third.level = 3
                            group_level_third.parent_id = group_level_second.id
                            group_level_third.save()

                        # group level 4
                        group_level_four = GroupATC.objects.filter(
                            code=row['code_level4']).first()
                        if group_level_four is None:
                            group_level_four.code = code = row['code_level4']
                            group_level_four.name = row['name_level4']
                            group_level_four.level = 4
                            group_level_four.save()

                        physic.group_id = group_level_four.id
                        physic.save()

                        # search route
                        route = RouteAdministration.objects.filter(
                            name=row['route']).first()
                        if route is None:
                            route = RouteAdministration()
                            route.name = row['route']
                            route.physic_id = physic.id
                            route.save()

                        # search level prescription
                        prescription_level = PrescriptionLevel.objects.filter(
                            level=row['prescription_level']).first()
                        if prescription_level is None:
                            prescription_level = PrescriptionLevel()
                            prescription_level.level = row['prescription_level']
                            prescription_level.name = prescrption_level_values[
                                row['prescription_level']] if row[
                                                                  'prescription_level'] in prescrption_level_values else ''
                            prescription_level.physic_id = physic.id
                            prescription_level.save()

                        # care level 1
                        care_level1 = CareLevel.objects.filter(
                            level='I').first()
                        if care_level1 is None:
                            care_level1 = CareLevel()
                            care_level1.level = 'I'
                            care_level1.name = care_level_values[
                                'I'] if 'I' in care_level_values else ''
                        if row['care_level1'] == 'x':
                            care_level1.physics.append(physic)
                        care_level1.save()

                        # care level 2
                        care_level2 = CareLevel.objects.filter(
                            level='II').first()
                        if care_level2 is None:
                            care_level2 = CareLevel()
                            care_level2.level = 'II'
                            care_level2.name = care_level_values[
                                'II'] if 'II' in care_level_values else ''
                        if row['care_level2'] == 'x':
                            care_level2.physics.append(physic)
                        care_level2.save()

                        # care level 3
                        care_level3 = CareLevel.objects.filter(
                            level='III').first()
                        if care_level3 is None:
                            care_level3 = CareLevel()
                            care_level3.level = 'III'
                            care_level3.name = care_level_values[
                                'III'] if 'III' in care_level_values else ''
                        if row['care_level3'] == 'x':
                            care_level3.physics.append(physic)
                        care_level3.save()

                        logging.info('row saved successfully')

                    else:
                        logging.warning('physic is already.')
            except IntegrityError:
                logging.error('row was not saved')
