# Generated by Django 2.1.7 on 2019-09-22 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20190922_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='aspects',
            new_name='goals',
        ),
    ]