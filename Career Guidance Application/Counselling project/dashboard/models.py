from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib

# Create your models here.
Gender = (
    (0, 'M'),
    (1, 'F'),
)




class Data(models.Model):
    Rank = models.PositiveIntegerField( null=True)
    India = models.PositiveIntegerField(null=True)
    Ethiopia=models.PositiveIntegerField(null=True)
    Nepal=models.PositiveIntegerField(null=True)
    Tenth = models.PositiveIntegerField(null=True)
    Twelth = models.PositiveIntegerField( null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/counselling_mod.joblib')
        self.predictions = ml_model.predict(
            [[self.Rank, self.India,self.Ethiopia,self.Nepal, self.Tenth ,self.Twelth]])
        return super().save(*args, *kwargs)
        
    class Meta:
        ordering = ['-date']
   

    def __str__(self):
        return self.name
