from rest_framework.serializers import ValidationError


class SalesElectroValidators:

    def __call__(self, value):
        val = dict(value)

        # Проверка зависимости иерархии типа завода с поставщиком
        if val.get("electro_type") == "FA":
            if val.get("supplier") and val.get("supplier").electro_type in ["NW", "IE"]:
                raise ValidationError("У завода не может быть данного поставщика")

        # Проверка зависимости иерархии типа розничной сети с поставщиком
        if val.get("electro_type") == "NW":
            if val.get("supplier") and val.get("supplier").electro_type in "IE":
                raise ValidationError(
                    "У розничной сети не может быть данного поставщика"
                )