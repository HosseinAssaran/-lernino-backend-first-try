# Generated by Django 2.1.1 on 2019-04-02 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_auto_20190402_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='apa_last_version',
            new_name='app_last_version',
        ),
    ]
