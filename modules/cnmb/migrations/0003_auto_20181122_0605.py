# Generated by Django 2.1.2 on 2018-11-22 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cnmb', '0002_auto_20181117_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concentration',
            name='measure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='concentrations', to='cnmb.Measure'),
        ),
        migrations.AlterField(
            model_name='physic',
            name='concentration',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='physics', to='cnmb.Concentration'),
        ),
    ]
