from django.urls import path
from mpesa.apis.views import LNMOnlineCreateAPIView

urlpatterns = [
    path("lnm/", LNMOnlineCreateAPIView.as_view(), name="lnm-callbackurl"),
]
