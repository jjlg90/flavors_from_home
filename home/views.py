from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(
                    subject, message, body['email'], [
                        'flavorsfromhomebv@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect("success")

    form = ContactForm()
    return render(request, "home/contact.html", {'form': form})


def success(request):
    """
    A view to return the success page after an email was sent.
    """
    return render(request, 'home/contact_success.html')
