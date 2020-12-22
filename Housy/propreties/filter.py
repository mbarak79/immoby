property_status = {
    'for sale': 'For Sale',
    'for Rent': 'For Rent'
}

property_types = {
    'appartment' : 'Appartments',
    'house'      : 'House',
    'commercial'  : 'Commercial',
}

Location = {
    'Paris' : 'Paris',
    'Marseille' : 'Marseille',
    'Bordeaux' : 'Bordeaux',
    'Toulouse' : 'Toulouse',
    'Strasbourg': 'Strasbourg',
    'Nantes' : 'Nantes',
    'Lyon'   : 'Lyon',
    'Montpellier' : 'Montpellier',
}

Bedrooms = {
    '1' : '1',
    '2' : '2',
    '3' : '3',
    '4' : '4',
    '5' : '5',
    '6' : '6',
}

Bathrooms = {
    '1' : '1',
    '2' : '2',
    '3' : '3',
    '4' : '4',
    '5' : '5',
    '6' : '6',
}

import django_filters
from .models import Properties
class PropertyFilter(django_filters.FilterSet):

    class Meta:
        model = Properties
        fields = ['city', 'property_types', 'property_status', 'bedrooms', 'bathrooms']


        