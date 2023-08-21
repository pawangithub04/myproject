# myproject/urls.py

from django.urls import path
from myapp.views import contact_form, home, about_us8aug, bytedigital, thankyou
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact_form, name='contact_form'),
    path('about_us8aug/', about_us8aug, name='about_us8aug'),
    path('bytedigital/', bytedigital, name='bytedigital'),
    path('thankyou/', thankyou, name='thankyou'),





]
