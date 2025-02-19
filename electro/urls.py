from django.urls import path

from electro.apps import ElectroConfig
from electro.views import (SalesElectroCreateApiView,
                           SalesElectroDestroyApiView, SalesElectroListApiView,
                           SalesElectroRetrieveApiView,
                           SalesElectroUpdateApiView)

app_name = ElectroConfig.name

urlpatterns = [
    path("electro/", SalesElectroListApiView.as_view(), name="electro-list"),
    path("electro/create/", SalesElectroCreateApiView.as_view(), name="electro-create"),
    path(
        "electro/<int:pk>/",
        SalesElectroRetrieveApiView.as_view(),
        name="electro-retrieve",
    ),
    path(
        "electro/<int:pk>/update/",
        SalesElectroUpdateApiView.as_view(),
        name="electro-update",
    ),
    path(
        "Electro/<int:pk>/delete/",
        SalesElectroDestroyApiView.as_view(),
        name="Electro-delete",
    ),
]