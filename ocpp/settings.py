from django.conf import settings


AMQP_URL = getattr(settings, "AMQP_URL")
OCPP_HEARTBEAT_INTERVAL = getattr(settings, "OCPP_HEARTBEAT_INTERVAL", 3600)
