# Generated by Django 2.2.6 on 2019-10-31 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20191031_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='city',
            new_name='Table_city',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='financial',
            new_name='Table_financial',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='financial_group',
            new_name='Table_financial_group',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='month',
            new_name='Table_month',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='office',
            new_name='Table_office',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='to',
            new_name='Table_to',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='value',
            new_name='Table_value',
        ),
        migrations.AlterModelTable(
            name='table',
            table='Table',
        ),
    ]
