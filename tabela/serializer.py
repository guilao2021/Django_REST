from django.db.models import fields
from rest_framework import serializers
from tabela_precos.models import Tratamento

class TratamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamento
        fields = '__all__'