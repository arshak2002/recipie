from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipie(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/',null=True)
    ingrediance = models.TextField()
    instruction = models.TextField()
    cooking_time = models.PositiveIntegerField()

    def __str__(self) :
        return self.title
    
class Favorite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    recipie = models.ForeignKey(Recipie,on_delete=models.CASCADE)

    def __str__(self):
        return self.recipie.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    recipie = models.ForeignKey(Recipie,on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.FloatField()

    def __str__(self):
        return self.recipie.title
