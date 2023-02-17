from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_name = request.POST['car_name']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(car_id=car_id, car_name=car_name, user_id=user_id, first_name=first_name, last_name=last_name,
                          customer_need=customer_need, city=city, state=state, email=email, phone=phone,
                          message=message)

        contact.save()
        messages.success(request, 'Your Request Has Been Submitted, We Will Get Back to You Shortly.')
        return redirect('/cars/' + car_id)
