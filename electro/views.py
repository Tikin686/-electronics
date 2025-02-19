from rest_framework import filters, generics

from electro.models import SalesElectro
from electro.serializers import SalesElectroSerializer
from users.permissions import IsActive


class SalesElectroListApiView(generics.ListAPIView):
    """Просмотр участников сетей продаж, которые являются также поставщиками"""

    queryset = SalesElectro.objects.all()
    serializer_class = SalesElectroSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["country"]
    permission_classes = (IsActive,)


class SalesElectroCreateApiView(generics.CreateAPIView):
    """Создание нового участника сети продаж"""

    queryset = SalesElectro.objects.all()
    serializer_class = SalesElectroSerializer
    permission_classes = (IsActive,)


class SalesElectroRetrieveApiView(generics.RetrieveAPIView):
    """Просмотр информации о конкретном участнике сети продаж"""

    queryset = SalesElectro.objects.all()
    serializer_class = SalesElectroSerializer
    permission_classes = (IsActive,)


class SalesElectroUpdateApiView(generics.UpdateAPIView):
    """Изменение информации о конкретном участнике сети продаж"""

    queryset = SalesElectro.objects.all()
    serializer_class = SalesElectroSerializer
    permission_classes = (IsActive,)


class SalesElectroDestroyApiView(generics.DestroyAPIView):
    """Удаление участника сети продаж"""

    queryset = SalesElectro.objects.all()
    serializer_class = SalesElectroSerializer
    permission_classes = (IsActive,)