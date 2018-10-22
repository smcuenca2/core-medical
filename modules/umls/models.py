# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ambiglui(models.Model):
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMBIGLUI'


class Ambigsui(models.Model):
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMBIGSUI'


class Deletedcui(models.Model):
    pcui = models.CharField(db_column='PCUI', max_length=8)  # Field name made lowercase.
    pstr = models.TextField(db_column='PSTR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DELETEDCUI'


class Deletedlui(models.Model):
    plui = models.CharField(db_column='PLUI', max_length=10)  # Field name made lowercase.
    pstr = models.TextField(db_column='PSTR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DELETEDLUI'


class Deletedsui(models.Model):
    psui = models.CharField(db_column='PSUI', max_length=10)  # Field name made lowercase.
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    pstr = models.TextField(db_column='PSTR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DELETEDSUI'


class Mergedcui(models.Model):
    pcui = models.CharField(db_column='PCUI', max_length=8)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MERGEDCUI'


class Mergedlui(models.Model):
    plui = models.CharField(db_column='PLUI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MERGEDLUI'


class Mraui(models.Model):
    aui1 = models.CharField(db_column='AUI1', max_length=9)  # Field name made lowercase.
    cui1 = models.CharField(db_column='CUI1', max_length=8)  # Field name made lowercase.
    ver = models.CharField(db_column='VER', max_length=10)  # Field name made lowercase.
    rel = models.CharField(db_column='REL', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rela = models.CharField(db_column='RELA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mapreason = models.TextField(db_column='MAPREASON')  # Field name made lowercase.
    aui2 = models.CharField(db_column='AUI2', max_length=9)  # Field name made lowercase.
    cui2 = models.CharField(db_column='CUI2', max_length=8)  # Field name made lowercase.
    mapin = models.CharField(db_column='MAPIN', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRAUI'


class Mrcols(models.Model):
    col = models.CharField(db_column='COL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    des = models.CharField(db_column='DES', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='REF', max_length=40, blank=True, null=True)  # Field name made lowercase.
    min = models.PositiveIntegerField(db_column='MIN', blank=True, null=True)  # Field name made lowercase.
    av = models.DecimalField(db_column='AV', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    max = models.PositiveIntegerField(db_column='MAX', blank=True, null=True)  # Field name made lowercase.
    fil = models.CharField(db_column='FIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dty = models.CharField(db_column='DTY', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRCOLS'


class Mrconso(models.Model):
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    ts = models.CharField(db_column='TS', max_length=1)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    stt = models.CharField(db_column='STT', max_length=3)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.
    ispref = models.CharField(db_column='ISPREF', max_length=1)  # Field name made lowercase.
    aui = models.CharField(db_column='AUI', primary_key=True, max_length=9)  # Field name made lowercase.
    saui = models.CharField(db_column='SAUI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scui = models.CharField(db_column='SCUI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sdui = models.CharField(db_column='SDUI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sab = models.CharField(db_column='SAB', max_length=40)  # Field name made lowercase.
    tty = models.CharField(db_column='TTY', max_length=40)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=100)  # Field name made lowercase.
    str = models.TextField(db_column='STR')  # Field name made lowercase.
    srl = models.PositiveIntegerField(db_column='SRL')  # Field name made lowercase.
    suppress = models.CharField(db_column='SUPPRESS', max_length=1)  # Field name made lowercase.
    cvf = models.PositiveIntegerField(db_column='CVF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRCONSO'


class Mrcui(models.Model):
    cui1 = models.CharField(db_column='CUI1', max_length=8)  # Field name made lowercase.
    ver = models.CharField(db_column='VER', max_length=10)  # Field name made lowercase.
    rel = models.CharField(db_column='REL', max_length=4)  # Field name made lowercase.
    rela = models.CharField(db_column='RELA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mapreason = models.TextField(db_column='MAPREASON', blank=True, null=True)  # Field name made lowercase.
    cui2 = models.CharField(db_column='CUI2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    mapin = models.CharField(db_column='MAPIN', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRCUI'


class Mrdef(models.Model):
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    aui = models.CharField(db_column='AUI', max_length=9)  # Field name made lowercase.
    atui = models.CharField(db_column='ATUI', primary_key=True, max_length=11)  # Field name made lowercase.
    satui = models.CharField(db_column='SATUI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sab = models.CharField(db_column='SAB', max_length=40)  # Field name made lowercase.
    def_field = models.TextField(db_column='DEF')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    suppress = models.CharField(db_column='SUPPRESS', max_length=1)  # Field name made lowercase.
    cvf = models.PositiveIntegerField(db_column='CVF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRDEF'


class Mrdoc(models.Model):
    dockey = models.CharField(db_column='DOCKEY', max_length=50)  # Field name made lowercase.
    value = models.CharField(db_column='VALUE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=50)  # Field name made lowercase.
    expl = models.TextField(db_column='EXPL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRDOC'


class Mrfiles(models.Model):
    fil = models.CharField(db_column='FIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    des = models.CharField(db_column='DES', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fmt = models.TextField(db_column='FMT', blank=True, null=True)  # Field name made lowercase.
    cls = models.PositiveIntegerField(db_column='CLS', blank=True, null=True)  # Field name made lowercase.
    rws = models.PositiveIntegerField(db_column='RWS', blank=True, null=True)  # Field name made lowercase.
    bts = models.BigIntegerField(db_column='BTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRFILES'


class Mrhier(models.Model):
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    aui = models.CharField(db_column='AUI', max_length=9)  # Field name made lowercase.
    cxn = models.PositiveIntegerField(db_column='CXN')  # Field name made lowercase.
    paui = models.CharField(db_column='PAUI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sab = models.CharField(db_column='SAB', max_length=40)  # Field name made lowercase.
    rela = models.CharField(db_column='RELA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ptr = models.TextField(db_column='PTR', blank=True, null=True)  # Field name made lowercase.
    hcd = models.CharField(db_column='HCD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cvf = models.PositiveIntegerField(db_column='CVF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRHIER'


class Mrhist(models.Model):
    cui = models.CharField(db_column='CUI', max_length=8, blank=True, null=True)  # Field name made lowercase.
    sourceui = models.CharField(db_column='SOURCEUI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sab = models.CharField(db_column='SAB', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sver = models.CharField(db_column='SVER', max_length=40, blank=True, null=True)  # Field name made lowercase.
    changetype = models.TextField(db_column='CHANGETYPE', blank=True, null=True)  # Field name made lowercase.
    changekey = models.TextField(db_column='CHANGEKEY', blank=True, null=True)  # Field name made lowercase.
    changeval = models.TextField(db_column='CHANGEVAL', blank=True, null=True)  # Field name made lowercase.
    reason = models.TextField(db_column='REASON', blank=True, null=True)  # Field name made lowercase.
    cvf = models.PositiveIntegerField(db_column='CVF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRHIST'


class Mrmap(models.Model):
    mapsetcui = models.CharField(db_column='MAPSETCUI', max_length=8)  # Field name made lowercase.
    mapsetsab = models.CharField(db_column='MAPSETSAB', max_length=40)  # Field name made lowercase.
    mapsubsetid = models.CharField(db_column='MAPSUBSETID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    maprank = models.PositiveIntegerField(db_column='MAPRANK', blank=True, null=True)  # Field name made lowercase.
    mapid = models.CharField(db_column='MAPID', max_length=50)  # Field name made lowercase.
    mapsid = models.CharField(db_column='MAPSID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fromid = models.CharField(db_column='FROMID', max_length=50)  # Field name made lowercase.
    fromsid = models.CharField(db_column='FROMSID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fromexpr = models.TextField(db_column='FROMEXPR')  # Field name made lowercase.
    fromtype = models.CharField(db_column='FROMTYPE', max_length=50)  # Field name made lowercase.
    fromrule = models.TextField(db_column='FROMRULE', blank=True, null=True)  # Field name made lowercase.
    fromres = models.TextField(db_column='FROMRES', blank=True, null=True)  # Field name made lowercase.
    rel = models.CharField(db_column='REL', max_length=4)  # Field name made lowercase.
    rela = models.CharField(db_column='RELA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    toid = models.CharField(db_column='TOID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tosid = models.CharField(db_column='TOSID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    toexpr = models.TextField(db_column='TOEXPR', blank=True, null=True)  # Field name made lowercase.
    totype = models.CharField(db_column='TOTYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    torule = models.TextField(db_column='TORULE', blank=True, null=True)  # Field name made lowercase.
    tores = models.TextField(db_column='TORES', blank=True, null=True)  # Field name made lowercase.
    maprule = models.TextField(db_column='MAPRULE', blank=True, null=True)  # Field name made lowercase.
    mapres = models.TextField(db_column='MAPRES', blank=True, null=True)  # Field name made lowercase.
    maptype = models.CharField(db_column='MAPTYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mapatn = models.CharField(db_column='MAPATN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mapatv = models.TextField(db_column='MAPATV', blank=True, null=True)  # Field name made lowercase.
    cvf = models.PositiveIntegerField(db_column='CVF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRMAP'


class Mrrank(models.Model):
    rank = models.PositiveIntegerField(db_column='RANK')  # Field name made lowercase.
    sab = models.CharField(db_column='SAB', primary_key=True, max_length=40)  # Field name made lowercase.
    tty = models.CharField(db_column='TTY', max_length=40)  # Field name made lowercase.
    suppress = models.CharField(db_column='SUPPRESS', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRRANK'
        unique_together = (('sab', 'tty'),)


class Mrrel(models.Model):
    cui1 = models.CharField(db_column='CUI1', max_length=8)  # Field name made lowercase.
    aui1 = models.CharField(db_column='AUI1', max_length=9, blank=True, null=True)  # Field name made lowercase.
    stype1 = models.CharField(db_column='STYPE1', max_length=50)  # Field name made lowercase.
    rel = models.CharField(db_column='REL', max_length=4)  # Field name made lowercase.
    cui2 = models.CharField(db_column='CUI2', max_length=8)  # Field name made lowercase.
    aui2 = models.CharField(db_column='AUI2', max_length=9, blank=True, null=True)  # Field name made lowercase.
    stype2 = models.CharField(db_column='STYPE2', max_length=50)  # Field name made lowercase.
    rela = models.CharField(db_column='RELA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rui = models.CharField(db_column='RUI', primary_key=True, max_length=10)  # Field name made lowercase.
    srui = models.CharField(db_column='SRUI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sab = models.CharField(db_column='SAB', max_length=40)  # Field name made lowercase.
    sl = models.CharField(db_column='SL', max_length=40)  # Field name made lowercase.
    rg = models.CharField(db_column='RG', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dir = models.CharField(db_column='DIR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    suppress = models.CharField(db_column='SUPPRESS', max_length=1)  # Field name made lowercase.
    cvf = models.PositiveIntegerField(db_column='CVF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRREL'


class Mrsab(models.Model):
    vcui = models.CharField(db_column='VCUI', max_length=8, blank=True, null=True)  # Field name made lowercase.
    rcui = models.CharField(db_column='RCUI', max_length=8, blank=True, null=True)  # Field name made lowercase.
    vsab = models.CharField(db_column='VSAB', primary_key=True, max_length=40)  # Field name made lowercase.
    rsab = models.CharField(db_column='RSAB', max_length=40)  # Field name made lowercase.
    son = models.TextField(db_column='SON')  # Field name made lowercase.
    sf = models.CharField(db_column='SF', max_length=40)  # Field name made lowercase.
    sver = models.CharField(db_column='SVER', max_length=40, blank=True, null=True)  # Field name made lowercase.
    vstart = models.CharField(db_column='VSTART', max_length=8, blank=True, null=True)  # Field name made lowercase.
    vend = models.CharField(db_column='VEND', max_length=8, blank=True, null=True)  # Field name made lowercase.
    imeta = models.CharField(db_column='IMETA', max_length=10)  # Field name made lowercase.
    rmeta = models.CharField(db_column='RMETA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    slc = models.TextField(db_column='SLC', blank=True, null=True)  # Field name made lowercase.
    scc = models.TextField(db_column='SCC', blank=True, null=True)  # Field name made lowercase.
    srl = models.PositiveIntegerField(db_column='SRL')  # Field name made lowercase.
    tfr = models.PositiveIntegerField(db_column='TFR', blank=True, null=True)  # Field name made lowercase.
    cfr = models.PositiveIntegerField(db_column='CFR', blank=True, null=True)  # Field name made lowercase.
    cxty = models.CharField(db_column='CXTY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ttyl = models.CharField(db_column='TTYL', max_length=400, blank=True, null=True)  # Field name made lowercase.
    atnl = models.TextField(db_column='ATNL', blank=True, null=True)  # Field name made lowercase.
    lat = models.CharField(db_column='LAT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cenc = models.CharField(db_column='CENC', max_length=40)  # Field name made lowercase.
    curver = models.CharField(db_column='CURVER', max_length=1)  # Field name made lowercase.
    sabin = models.CharField(db_column='SABIN', max_length=1)  # Field name made lowercase.
    ssn = models.TextField(db_column='SSN')  # Field name made lowercase.
    scit = models.TextField(db_column='SCIT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRSAB'


class Mrsat(models.Model):
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    metaui = models.CharField(db_column='METAUI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stype = models.CharField(db_column='STYPE', max_length=50)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    atui = models.CharField(db_column='ATUI', primary_key=True, max_length=11)  # Field name made lowercase.
    satui = models.CharField(db_column='SATUI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    atn = models.CharField(db_column='ATN', max_length=100)  # Field name made lowercase.
    sab = models.CharField(db_column='SAB', max_length=40)  # Field name made lowercase.
    atv = models.TextField(db_column='ATV', blank=True, null=True)  # Field name made lowercase.
    suppress = models.CharField(db_column='SUPPRESS', max_length=1)  # Field name made lowercase.
    cvf = models.PositiveIntegerField(db_column='CVF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRSAT'


class Mrsmap(models.Model):
    mapsetcui = models.CharField(db_column='MAPSETCUI', max_length=8)  # Field name made lowercase.
    mapsetsab = models.CharField(db_column='MAPSETSAB', max_length=40)  # Field name made lowercase.
    mapid = models.CharField(db_column='MAPID', max_length=50)  # Field name made lowercase.
    mapsid = models.CharField(db_column='MAPSID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fromexpr = models.TextField(db_column='FROMEXPR')  # Field name made lowercase.
    fromtype = models.CharField(db_column='FROMTYPE', max_length=50)  # Field name made lowercase.
    rel = models.CharField(db_column='REL', max_length=4)  # Field name made lowercase.
    rela = models.CharField(db_column='RELA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    toexpr = models.TextField(db_column='TOEXPR', blank=True, null=True)  # Field name made lowercase.
    totype = models.CharField(db_column='TOTYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cvf = models.PositiveIntegerField(db_column='CVF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRSMAP'


class Mrsty(models.Model):
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    tui = models.CharField(db_column='TUI', max_length=4)  # Field name made lowercase.
    stn = models.CharField(db_column='STN', max_length=100)  # Field name made lowercase.
    sty = models.CharField(db_column='STY', max_length=50)  # Field name made lowercase.
    atui = models.CharField(db_column='ATUI', primary_key=True, max_length=11)  # Field name made lowercase.
    cvf = models.PositiveIntegerField(db_column='CVF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRSTY'


class MrxnsEng(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    nstr = models.TextField(db_column='NSTR')  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXNS_ENG'


class MrxnwEng(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    nwd = models.CharField(db_column='NWD', max_length=100)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXNW_ENG'


class MrxwBaq(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_BAQ'


class MrxwChi(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_CHI'


class MrxwCze(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_CZE'


class MrxwDan(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_DAN'


class MrxwDut(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_DUT'


class MrxwEng(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_ENG'


class MrxwEst(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_EST'


class MrxwFin(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_FIN'


class MrxwFre(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_FRE'


class MrxwGer(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_GER'


class MrxwGre(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_GRE'


class MrxwHeb(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_HEB'


class MrxwHun(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_HUN'


class MrxwIta(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_ITA'


class MrxwJpn(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=500)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_JPN'


class MrxwKor(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=500)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_KOR'


class MrxwLav(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_LAV'


class MrxwNor(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_NOR'


class MrxwPol(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_POL'


class MrxwPor(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_POR'


class MrxwRus(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_RUS'


class MrxwScr(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_SCR'


class MrxwSpa(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_SPA'


class MrxwSwe(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_SWE'


class MrxwTur(models.Model):
    lat = models.CharField(db_column='LAT', max_length=3)  # Field name made lowercase.
    wd = models.CharField(db_column='WD', max_length=200)  # Field name made lowercase.
    cui = models.CharField(db_column='CUI', max_length=8)  # Field name made lowercase.
    lui = models.CharField(db_column='LUI', max_length=10)  # Field name made lowercase.
    sui = models.CharField(db_column='SUI', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MRXW_TUR'
