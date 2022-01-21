from django.db import models
from django.urls import reverse

FUEL = (
    ('R', 'Regular'),
    ('M', 'Midgrade'),
    ('P', 'Premium')
)

# Create your models here.

class Paint(models.Model):
  color = models.CharField(max_length=50)
  finish = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('paint_detail', kwargs={'pk': self.id})

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    year = models.IntegerField()
    paint = models.ManyToManyField(Paint)

    def __str__(self):
        return self.make + ' ' + self.model

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Fueling(models.Model):
    date = models.DateField('fueling date')
    fuel = models.CharField(
      max_length=1, 
      choices=FUEL,
      default=FUEL[0][0])

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_fuel_display()} on {self.date}"

    class Meta:
        ordering = ['-date']



