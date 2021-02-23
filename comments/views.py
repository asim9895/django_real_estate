from django.shortcuts import render, redirect
from .models import Comment
from django.contrib import messages


# Create your views here.

def comment(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_name = request.POST['realtor_name']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Comment.objects.all().filter(listing_id=listing_id , user_id=user_id)

            if has_contacted:
                messages.error(request ,' You already post an inquiry on this listing')
                return redirect('/listings/'+listing_id)


        comment = Comment(
            listing_id=listing_id,
            listing=listing,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
            
        )

        comment.save()

        

        messages.success(request , f'Your request has been submitted , {realtor_name} will get back to you soon')
        return redirect('/listings/'+listing_id)

