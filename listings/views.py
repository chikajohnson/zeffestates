from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import bedroom_choices, price_choices, state_choices
from .models import Listing

def index(request):
   listings = Listing.objects.order_by('-list_date').filter(is_published=True)

   paginator = Paginator(listings, 3)
   page = request.GET.get('page')
   page_listings = paginator.get_page(page)

   context = {
      'listings': page_listings
   }
   return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
   listing = get_object_or_404(Listing, pk=listing_id)
   context = {
      'listing': listing
   }
   return  render(request, 'listings/listing.html', context)

def search(request):
   queryset_list = Listing.objects.order_by('-list_date')

   # Kewords
   if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      if keywords:
        queryset_list = queryset_list.filter(description__icontains=keywords)  

   # city
   if 'city' in request.GET:
      keywords = request.GET['city']
      if keywords:
        queryset_list = queryset_list.filter(city__iexact=keywords) 
   
   # state
   if 'state' in request.GET:
      keywords = request.GET['state']
      if keywords:
        queryset_list = queryset_list.filter(state__iexact=keywords)  

    # bedrooms
   if 'bedrooms' in request.GET:
      keywords = request.GET['bedrooms']
      if keywords:
        queryset_list = queryset_list.filter(bedrooms__lte=keywords)       

     # price
   if 'price' in request.GET:
      keywords = request.GET['price']
      if keywords:
        queryset_list = queryset_list.filter(price__lte=keywords)       

   context = {
      'price_choices': price_choices,
      'bedroom_choices': bedroom_choices,
      'state_choices': state_choices,
      'listings': queryset_list,
      'search_values': request.GET
   }

   return render(request, 'listings/search.html', context)