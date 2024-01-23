from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Email
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            validate_email(email)
            if not Email.objects.filter(address=email).exists():
                new_email = Email(address=email)
                new_email.save()
            return render(request, 'index.html', {'success_message': 'Email unsubscribed successfully'})
        except ValidationError:
            return render(request, 'index.html', {'warning_message': 'Please enter a valid email address'})
    else:
        return render(request, 'index.html')


def download_emails(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == 'admin':
            emails = Email.objects.all()
            email_list = "\n".join([str(email) for email in emails])
            response = HttpResponse(email_list, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename="emails.txt"'
            return response
        else:
            return render(request, 'download.html', {'error_message': 'Invalid password'})

    return render(request, 'download.html')