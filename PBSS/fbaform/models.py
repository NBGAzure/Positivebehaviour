from django.db import models

class Location(models.Model):
    wakingup = models.CharField(max_length=255)
    # pain = models.CharField(max_length=255)
    # staff = models.CharField(max_length=255)
    # solution = models.CharField(max_length=255)


class Triggers(models.Model):
    reason1 = models.CharField(max_length=255)
#     reason2 = models.CharField(max_length=255)
#     reason3 = models.CharField(max_length=255)
#     reason4 = models.CharField(max_length=255)
#     reason5 = models.CharField(max_length=255)

# class CuesOfDistress(models.Model):
#     cues1 = models.CharField(max_length=255)
    # cues2 = models.CharField(max_length=255)
#     cues3 = models.CharField(max_length=255)
#     cues4 = models.CharField(max_length=255)
#     cues5 = models.CharField(max_length=255)
#     cues6 = models.CharField(max_length=255)
