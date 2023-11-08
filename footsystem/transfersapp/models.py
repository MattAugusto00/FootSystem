from django.db import models

class Clube(models.Model):
    id_clube = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)

class Jogador(models.Model):
    id_jogador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    clube_atual = models.ForeignKey(Clube, on_delete=models.CASCADE)

class Transferencia(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    clube_origem = models.ForeignKey(Clube, related_name='transferencias_origem', on_delete=models.CASCADE)
    clube_destino = models.ForeignKey(Clube, related_name='transferencias_destino', on_delete=models.CASCADE)
    valor = models.IntegerField()
    data_transferencia = models.DateField()
