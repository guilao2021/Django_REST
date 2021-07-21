from rest_framework import serializers, viewsets, generics
from tabela_precos.models import Tratamento
from tabela_precos.serializer import TratamentoSerializer

class TratamentosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Tratamento.objects.all()
    serializer_class = TratamentoSerializer
