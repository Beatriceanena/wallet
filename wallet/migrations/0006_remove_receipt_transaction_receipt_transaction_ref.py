# Generated by Django 4.0.6 on 2022-08-02 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_rename_notifications_notification_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='transaction',
        ),
        migrations.AddField(
            model_name='receipt',
            name='transaction_ref',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
