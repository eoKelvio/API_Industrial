from django.db import models

class Entity(models.Model):
    sensor = models.BooleanField(default=False)
    botao = models.BooleanField(default=False)
    ligaRobo = models.BooleanField(default=False)
    resetContador = models.BooleanField(default=False)
    valorContagem = models.IntegerField(default=0)

    def _str_(self):
        return "Category Entity [%s]" % self.category