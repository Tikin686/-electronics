from rest_framework.serializers import ModelSerializer

from electro.models import SalesElectro
from electro.validators import SalesElectroValidators


class SalesElectroSerializer(ModelSerializer):
    """Сериализатор для модели SalesElectro"""

    class Meta:
        model = SalesElectro
        fields = "__all__"
        read_only_fields = ["debt"]
        validators = [SalesElectroValidators()]