from django import forms
from .models import Review
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email']  # Add or remove fields as needed

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise ValidationError("Passwords do not match")

        return cleaned_data


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'my_team',
            'team_visited',
            'visit_date',
            'final_score',
            'result',
            'location_rating',
            'atmosphere_rating',
            'facilities_rating',
            'catering_rating',
            'overall_rating',
            'comments',
        ]
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }