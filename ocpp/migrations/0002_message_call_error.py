# Generated by Django 4.1.7 on 2023-03-31 05:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ocpp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="error_code",
            field=models.CharField(
                blank=True,
                choices=[
                    ("NotImplemented", "NotImplemented"),
                    ("NotSupported", "NotSupported"),
                    ("InternalError", "InternalError"),
                    ("ProtocolError", "ProtocolError"),
                    ("SecurityError", "SecurityError"),
                    ("FormationViolation", "FormationViolation"),
                    ("PropertyConstraintViolation", "PropertyConstraintViolation"),
                    ("OccurenceConstraintViolation", "OccurenceConstraintViolation"),
                    ("TypeConstraintViolation", "TypeConstraintViolation"),
                    ("GenericError", "GenericError"),
                ],
                max_length=64,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="error_description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="stop_reason",
            field=models.CharField(
                blank=True,
                choices=[
                    ("EmergencyStop", "EmergencyStop"),
                    ("EVDisconnected", "EVDisconnected"),
                    ("HardReset", "HardReset"),
                    ("Local", "Local"),
                    ("Other", "Other"),
                    ("PowerLoss", "PowerLoss"),
                    ("Reboot", "Reboot"),
                    ("Remote", "Remote"),
                    ("SoftReset", "SoftReset"),
                    ("UnlockCommand", "UnlockCommand"),
                    ("DeAuthorized", "DeAuthorized"),
                ],
                max_length=64,
                null=True,
            ),
        ),
    ]
