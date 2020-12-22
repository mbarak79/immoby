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


class Property_types(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Property_status(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class FeaturedProperties(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Houses')
    image1 = models.ImageField(upload_to='Houses', blank=True, null=True )
    image2 = models.ImageField(upload_to='Houses', blank=True, null=True)
    image3 = models.ImageField(upload_to='Houses', blank=True, null=True)
    image4 = models.ImageField(upload_to='Houses', blank=True, null=True)
    image5 = models.ImageField(upload_to='Houses', blank=True, null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(choices= CITY , max_length=200, default='City')
    sqft    = models.FloatField()
    price    = models.PositiveIntegerField(default=1)
    bedrooms = models.PositiveIntegerField()
    bathrooms  = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now=True)
    property_types = models.ForeignKey(Property_types, on_delete=models.CASCADE)
    property_status = models.ForeignKey(Property_status, on_delete=models.CASCADE)
    cp      = models.PositiveIntegerField(null=True)
    owner = models.CharField(max_length=100)
    terrasse   = models.BooleanField(default=False)
    balcony  = models.PositiveIntegerField(null=True)
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.address
    class Meta:
        ordering = ['-created']
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(FeaturedProperties, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('details', kwargs={'slug':self.slug})



