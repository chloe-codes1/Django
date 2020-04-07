from django import forms
from .models import Article

#Form 사용

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
                max_length=100,
                label='Title',
                help_text='Your title should be less than 100 words',
                widget=forms.TextInput(
                    attrs={
                        'class':'my_input',
                        'placeholder': 'Type the tile'
                    }
                ))

    content = forms.CharField(
                label='Content',
                help_text='Jot down random musings',
                widget=forms.Textarea(
                    attrs={
                        'row':5,
                        'col':50,
                    }
                )
    )
    class Meta:
        model = Article
        fields = ['title', 'content']