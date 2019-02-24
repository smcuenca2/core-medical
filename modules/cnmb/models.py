from django.contrib.auth.models import User
from django.db import models


class Audit(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class GroupATC(Audit):
    TYPE_CHOICES = (
        ('ALFA', 'ALFA'),
        ('NUMERIC', 'NUMERICO'),
    )
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True, max_length=500)
    level = models.PositiveIntegerField(default=1)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.CASCADE)
    type = models.CharField(
        max_length=25,
        choices=TYPE_CHOICES,
        default='ALFA',
    )


class Measure(Audit):
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True, max_length=500)
    active = models.BooleanField(default=True)


class Concentration(Audit):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True, max_length=500)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=True)
    measure = models.ForeignKey(Measure, null=True,
                                related_name='concentrations',
                                on_delete=models.CASCADE)


class PhysicLevel(Audit):
    level = models.CharField(max_length=25)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True, max_length=500)
    active = models.BooleanField(default=True)


class PrescriptionLevel(PhysicLevel):

    def __repr__(self):
        self.name


class Physic(Audit):
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True, max_length=500)
    pharmaceuticalform = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    concentration = models.ForeignKey('cnmb.Concentration', null=True,
                                      related_name='physics',
                                      on_delete=models.CASCADE)
    group = models.ForeignKey('cnmb.GroupATC',
                              related_name='physics',
                              on_delete=models.CASCADE)

    prescription_level = models.ForeignKey('cnmb.PrescriptionLevel',
                                           related_name='physics',
                                           on_delete=models.CASCADE)


class CareLevel(PhysicLevel):
    physics = models.ManyToManyField('cnmb.Physic',
                                     related_name='cares')


class Use(Audit):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True, max_length=500)
    active = models.BooleanField(default=True)


class RouteAdministration(Use):
    physic = models.ForeignKey('cnmb.Physic',
                               related_name='routes_administration',
                               on_delete=models.CASCADE)

    def __repr__(self):
        self.name


class Range(Audit):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True, max_length=500)
    active = models.BooleanField(default=True)
    start = models.PositiveIntegerField(default=0)
    end = models.PositiveIntegerField(default=1)


class Dosification(Audit):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True, max_length=500)
    active = models.BooleanField(default=True)
    range = models.ForeignKey('cnmb.Range',
                              related_name='dosifications',
                              on_delete=models.CASCADE)
    route = models.ForeignKey('cnmb.RouteAdministration',
                              related_name='dosifications',
                              on_delete=models.CASCADE)
