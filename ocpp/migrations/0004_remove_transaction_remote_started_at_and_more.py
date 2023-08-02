# Generated by Django 4.1.7 on 2023-04-04 02:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ocpp", "0003_chargepoint_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transaction",
            name="remote_started_at",
        ),
        migrations.RemoveField(
            model_name="transaction",
            name="remote_stopped_at",
        ),
        migrations.AlterField(
            model_name="transaction",
            name="started_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="stopped_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
