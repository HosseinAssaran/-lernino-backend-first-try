# Generated by Django 2.1.1 on 2018-09-21 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20180916_1427'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='part',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='part',
            name='icon',
            field=models.CharField(choices=[('md-arrow-dropleft', 'Reading'), ('md-help-buoy', 'Question')], default=1, max_length=50),
        ),
    ]
