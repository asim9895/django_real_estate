from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages

# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        message = request.POST['message']

        contact = Contact(listing=listing , listing_id=listing_id,  name=name, email=email , 
           message=message , user_id=user_id , phone=phone)
        
        contact.save()

        messages.success(request , 'Your request has been submitted , a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)