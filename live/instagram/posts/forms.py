from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        label='Title',
        help_text='Your title must be no more than 100 characters in length',
        widget=forms.TextInput(
            attrs={
                'class':'my_input',
                'placeholder': "What's on your mind?"
            }
        )
    )
    content = forms.CharField(
        label='Content',
        help_text='Jot down random musings and thoughts',
        widget=forms.Textarea(
            attrs={
                'row':5,
                'col':50,
            }
        )
    )
    class Meta:
        model = Post
        # 다 때려박아
        fields = '__all__'

        # 제목은 못고치게 해볼까..
        # exclude = ['title']

    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']