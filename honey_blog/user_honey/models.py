from django.db import models



class UserHoney(models.Model):
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE)
    honey = models.ForeignKey(
        'honey_app.Honey',
        on_delete=models.CASCADE)
