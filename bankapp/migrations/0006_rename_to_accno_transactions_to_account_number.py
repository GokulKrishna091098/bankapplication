# Generated by Django 3.2 on 2021-05-21 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0005_transactions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='to_accno',
            new_name='to_account_number',
        ),
    ]
