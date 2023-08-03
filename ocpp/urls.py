from .views import SimulatorView
from django.urls import path

urlpatterns = [
    path("", SimulatorView.as_view(), name="ocpp_demo"),
]
