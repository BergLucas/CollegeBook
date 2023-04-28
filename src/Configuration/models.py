from django.db import models

from Account.models import User


class Config(models.Model):
    name = models.CharField('Nom de configuration', max_length=30, blank=True) #pour l'instant tout les profs on les 4 configs principales mais on devrait changer
    seating_arrangement = models.JSONField("Disposition de la salle", blank=True, null=True) #TODO retirer le blank ensuite mais pour teste ici
    url_json = models.CharField('URL du fichier json', max_length=100, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Place(models.Model):
    type = models.CharField("Nom de la place", max_length=50)
    price = models.DecimalField("Prix de la place", max_digits=5, decimal_places=2)

    configuration = models.ForeignKey(Config, on_delete=models.CASCADE)