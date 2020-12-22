from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import FeaturedProperties, Property_types
from .forms import SignUpForm
from .filter import property_status, property_types, Location, Bathrooms, Bedrooms
from django.core.paginator import PageNotAnInteger, Paginator, Page,EmptyPage
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count 


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'houses/signup.html', {'form': form})

def index(request):
    features = FeaturedProperties.objects.all()
    recently = FeaturedProperties.objects.all().order_by('-created')
    stat_type = features.count()

    paginator = Paginator(features, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'features' :  page_obj,
        'property_status' : property_status,
        'property_types' : property_types,
        'Location' : Location,
        'Bedrooms' : Bedrooms,
        'Bathrooms' : Bathrooms,
        'recently' : recently,
        'stat_type' : stat_type,
        
    }
    return render(request, 'houses/index.html', context)

def details(request, slug):
    prop_details = FeaturedProperties.objects.get(slug=slug)
    cat_type = Property_types.objects.filter().annotate(title_count=Count('title'))

    context = {
        'prop_details': prop_details,
        'cat_type' : cat_type
    }
    return render(request, 'houses/properties-details-2.html', context)



def services(request):
    return render(request, 'houses/services.html')

def contact(request):
    return render(request, 'houses/contact.html')

    
       
    