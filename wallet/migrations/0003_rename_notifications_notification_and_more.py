# Generated by Django 4.0.6 on 2022-08-01 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_alter_currency_amount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notifications',
            new_name='Notification',
        ),
        migrations.RenameModel(
            old_name='Receipts',
            new_name='Receipt',
        ),
    ]
