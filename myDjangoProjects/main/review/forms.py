from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'category']

        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control','placeholder': 'Введите свое имя'}),
            "content": forms.Textarea(attrs={'class': 'form-control','placeholder': 'Напишите отзыв'}),
            "category": forms.Select(attrs={'class': 'form-control',"placeholder": 'услуга'})
        }
