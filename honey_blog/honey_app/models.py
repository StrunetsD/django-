from django.core.validators import MinValueValidator
from django.db import models



class Honey(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(validators=[MinValueValidator(1)], max_digits=5, decimal_places=2)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='honey_images/')

    def __str__(self):
        return self.name

class Comment(models.Model):
    honey = models.ForeignKey('honey_app.Honey', on_delete=models.CASCADE)
    text = models.TextField(null = False)
    created_at = models.DateTimeField(auto_now_add=True, null = True)
    user = models.ForeignKey('user_honey.UserHoney', on_delete=models.CASCADE)

    def __str__(self):
        return self.text