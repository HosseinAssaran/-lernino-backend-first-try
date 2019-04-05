# Generated by Django 2.1.1 on 2019-04-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0022_auto_20190402_0512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='apkLastVersion',
            new_name='apa_last_version',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='apkAddress',
            new_name='app_address',
        ),
        migrations.RemoveField(
            model_name='school',
            name='apkForceUpdate',
        ),
        migrations.AddField(
            model_name='school',
            name='app_force_update',
            field=models.BooleanField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='school',
            name='app_text_message',
            field=models.TextField(null=True),
        ),
    ]
