from django.shortcuts import render
from houses.models import FeaturedProperties
from houses.models import FeaturedProperties
from .filter import property_status, property_types, Bedrooms, Bathrooms, Location, PropertyFilter

# Create your views here.


def propreties(request):
    propreties = FeaturedProperties.objects.all()

    myFilter = PropertyFilter(request.GET, queryset=propreties)
    propreties = myFilter.qs

    context = {
        'propreties' :  propreties,
        'property_status': property_status,
        'property_types': property_types,
        'Location': Location,
        'Bedrooms': Bedrooms,
        'Bathrooms': Bathrooms,
        'myFilter': myFilter
    }
    return render(request, 'propreties/listings.html', context)


