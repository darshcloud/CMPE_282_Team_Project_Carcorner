from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User


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

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/cars/'+car_id)

        contact = Contact(car_id=car_id, car_name=car_name, user_id=user_id, first_name=first_name, last_name=last_name,
                          customer_need=customer_need, city=city, state=state, email=email, phone=phone,
                          message=message)

        

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                'New Car Inquiry',
                'You have a new inquiry for the car ' + car_name + '. Please login to your admin panel for more info.',
                'carcorneradmin@gmail.com',
                ['carcornerdeveloper@gmail.com'],
                fail_silently=False,
            )

        contact.save()
        messages.success(request, 'Your Request Has Been Submitted, We Will Get Back to You Shortly.')
        return redirect('/cars/' + car_id)
