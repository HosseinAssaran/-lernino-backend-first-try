# Generated by Django 2.1.1 on 2018-10-16 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_lesson_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='school',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons_school', to='courses.School'),
        ),
    ]
