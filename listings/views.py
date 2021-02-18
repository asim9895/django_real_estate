
from typing import List
from django.core import paginator
from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import PageNotAnInteger , EmptyPage , Paginator
from .choices import state_choices , price_choices , bedroom_choices


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings , 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request , 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing , pk=listing_id)

    context = {
        'listing': listing,
    }
    return render(request , 'listings/listing.html' , context)

def search(request):
    query_listing = Listing.objects.order_by('-list_date')
     
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_listing = query_listing.filter(description__icontains=keywords)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_listing = query_listing.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_listing = query_listing.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_listing = query_listing.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_listing = query_listing.filter(price__lte=price)



    context = {
        'listings': query_listing,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.GET
    }
    return render(request , 'listings/search.html', context)

