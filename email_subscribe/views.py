from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from .models import Subscription
import uuid

@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        city = request.POST.get('city')
        token = str(uuid.uuid4())
        subscription, created = Subscription.objects.get_or_create(
            email=email, city=city, defaults={'confirmation_token': token}
        )
        if created:
            send_confirmation_email(email, token)
        else:
            if not subscription.confirmed:
                subscription.confirmation_token = token
                subscription.save()
                send_confirmation_email(email, token)
        return JsonResponse({'message': 'Please check your email to confirm your subscription.'})

@csrf_exempt
def unsubscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        city = request.POST.get('city')
        subscription = get_object_or_404(Subscription, email=email, city=city)
        subscription.delete()
        return JsonResponse({'message': 'You have been unsubscribed.'})

def confirm_subscription(request, token):
    subscription = get_object_or_404(Subscription, confirmation_token=token)
    subscription.confirmed = True
    subscription.save()
    return JsonResponse({'message': 'Subscription confirmed!'})

def send_confirmation_email(email, token):
    confirm_url = f'https://frontend-ten-xi-92.vercel.app/email/confirm/{token}/'
    send_mail(
        'Confirm your subscription',
        f'Click the link to confirm your subscription: {confirm_url}',
        settings.DEFAULT_FROM_EMAIL,
        [email],
    )
