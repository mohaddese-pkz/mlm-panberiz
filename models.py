from django.db import models
from Users.models import Users


class UserOwner(models.Model):

    MlmOwner = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='userOwner', null=True, blank=True)
    MlmUser = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)



class Category(models.Model):

    OwnerCategory = models.CharField(max_length=90, verbose_name='ownercategory')
    stars = models.IntegerField(null=True, blank=True, verbose_name='stars')
    Id = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)


class Compress(models.Model):

    CMlmOwner = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='Compress', null=True, blank=True)
    CMlmUser = models.ForeignKey(Users, on_delete=models.CASCADE)