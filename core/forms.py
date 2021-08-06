from django import forms
import django.forms.widgets
from django.contrib.auth.models import User


class GetEmailForm(forms.ModelForm):
    email = forms.EmailField(label=False, widget=forms.EmailInput(
        attrs={'placeholder': 'Почта ...', 'class': 'tricks-sidebar__mail'}))

    class Meta:
        model = User
        fields = ['email']
