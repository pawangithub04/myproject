# myapp/views.py

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about_us8aug(request):
    return render(request, 'about_us8aug.html')

def bytedigital(request):
    return render(request, 'bytedigital.html')

def thankyou(request):
    return render(request, 'thankyou.html')



def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        phone_no = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        selected_services = request.POST.getlist('services')
        print(selected_services)
        # ux_ui_design = request.POST.get('UX and UI Design', '')
        # web_development = request.POST.get('Web development', '')
        # selected_services = [service for service in [ux_ui_design, web_development] if service]

        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}\nPhone_no: {phone_no}\nSubject: {subject}\nI am looking for: {", ".join(selected_services)}',
            #f'Name: {name}\nEmail: {email}\nMessage: {message}\nPhone_no: {phone_no}\nSubject: {subject}',

            'email',
            ['vintee.mishra@byte-digital.com.au','sharma@byte-digital.com.au'],
            fail_silently=False,
        )
        send_mail(
            'Thank You For Contacting Us',
            f"Dear Client\nThank You for your valuable inquiry,We will get back to you soon.\nRegards:\nSupport team\nByte Digital Consulting Pvt Ltd\n",
            {email},


            [email],
            fail_silently=False,
        )


    return render(request, 'form.html')



# from .forms import ContactForm
#
# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Process the form data (e.g., send an email)
#             # Add your logic here
#
#             # Optionally, you can show a success message and redirect to a thank you page
#             return render(request, 'contact/thank_you.html')
#     else:
#         form = ContactForm()
#
#     return render(request, 'contact/contact_form.html', {'form': form})
