from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.


PROPRETY_TYPE = (
    ('appartment' , 'Appartment'),
    ('house'      , 'House'),
    ('commercial' , 'Commercial')
)

PROPRETY_STATUS = (
    ('for sale' , 'For Sale'),
    ('for rent'      , 'For Rent',)
    
)

CITY = (
    ('Paris' , 'Paris'),
    ('Marseille' , 'Marseille'),
    ('Bordeaux' , 'Bordeaux'),
    ('Toulouse' , 'Toulouse'),
    ('Strasbourg', 'Strasbourg'),
    ('Nantes' , 'Nantes'),
    ('lyon'   , 'Lyon'),
    ('Montpellier' , 'Montpellier'),
)

class Properties(models.Model):
    title = models.CharField(max_length=100, unique=True)
    owner = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(choices= CITY , max_length=200, default='Appartment')
    image = models.ImageField(upload_to='Houses')
    address = models.CharField(max_length=100)
    sqft    = models.FloatField()
    property_types = models.CharField(choices= PROPRETY_TYPE , max_length=200, default='Appartment')
    property_status = models.CharField(choices= PROPRETY_STATUS , max_length=200, default='For Sale')
    bedrooms = models.PositiveIntegerField()
    bathrooms  = models.PositiveIntegerField()
    price  = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now=True)
    balcony      = models.PositiveIntegerField(null=True)
    cp      = models.PositiveIntegerField(null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.address
    class Meta:
        ordering = ['title', '-created']
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Properties, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug':self.slug})

    