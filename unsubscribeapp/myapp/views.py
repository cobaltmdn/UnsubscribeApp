from django.core.paginator import Paginator
from django.shortcuts import render, redirect
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


def get_emails(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == 'admin':
            return redirect('edit_emails')
        else:
            return render(request, 'download.html', {'error_message': 'Invalid password'})
    else:
        return render(request, 'download.html')


def edit_emails(request):
    email_list = Email.objects.all().order_by('id')
    paginator = Paginator(email_list, 200)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'edit_emails.html', {'page_obj': page_obj})


def delete_emails(request):
    if request.method == 'POST':
        selected_email_addresses = request.POST.getlist('emails')
        if selected_email_addresses:
            Email.objects.filter(address__in=selected_email_addresses).delete()
        return redirect('edit_emails')
    else:
        return render(request, 'download.html')


def download_emails(request):
    if request.method == 'POST':
        emails = Email.objects.all()
        email_list = "\n".join([str(email) for email in emails])
        response = HttpResponse(email_list, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="emails.txt"'
        return response
    else:
        return render(request, 'download.html')


def search_emails(request):
    query = request.GET.get('query', '')
    if query:
        emails = Email.objects.filter(address__icontains=query).order_by('id')
        paginator = Paginator(emails, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'edit_emails.html', {'page_obj': page_obj, 'query': query})
    else:
        return redirect('edit_emails')
