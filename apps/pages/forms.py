from django import forms
from django.forms import ModelForm
from .models import UserPost


class UserPostForm(ModelForm):
    class Meta:
        model = UserPost
        fields = ('title', 'body', 'photo', 'body2', 'photo2', 'body3', 'photo3' , 'body4', 'photo4' ,)

        labels = {
            'title': '',
            'body': '',
            'photo': '',
            'body2' : '',
            'photo2' : '',
            'body3': '',
            'photo3': '',
            'body4': '',
            'photo4': '',
            }
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sarlavha'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'1-matn'}),
            'body2': forms.Textarea(attrs={'class':'form-control', 'placeholder':'2-matn'}),
            'body3': forms.Textarea(attrs={'class':'form-control', 'placeholder':'3-matn'}),
            'body4': forms.Textarea(attrs={'class':'form-control', 'placeholder':'4-matn'}),
        }




