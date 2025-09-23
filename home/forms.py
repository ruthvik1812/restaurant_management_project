from django import forms
from .models import Contact
from .models import NewsletterSubscriber
from home.utils.validation_utils import is_valid_email

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name':forms.TextInput(attrs={'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailIntput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your mesaage  here', 'rows': 4}),

        }
    
    # Validate Email Field
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required!")
        if "@" not in email or "." not in email:
            raise forms.ValidationError("Enter a valid email address!")
        return email
    # Validate Message Field
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message or len(message.strip()) < 10:
            raise forms.ValidationError("Message must be atleast 10 characters long.")
        return message
    # Newsletter subscription Form
    class NewsletterForm(forms.ModelForm):
        class Meta:
            model = NewsletterSubscriber
            fields = ['email']
            widgets = {
                'email': forms.EmailIntput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your email to subscribe'
                }),
            }