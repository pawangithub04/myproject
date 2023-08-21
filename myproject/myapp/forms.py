from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email', max_length=100)
    address = forms.CharField(label='Address', max_length=200, required=False)
    message = forms.CharField(label='Your Message', widget=forms.Textarea)
    phone_no = forms.CharField(label='phone_no', widget=forms.Textarea)
