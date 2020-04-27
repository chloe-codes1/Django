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

        # 사용자가 글 작성자가 누군지 선택하게 하면 안되므로
        exclude = ['user']

    
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='Comment',
        help_text='What do you think about this post?',
        widget=forms.Textarea(
            attrs={
                'row':2,
                'col':10,
            }
        )
    )
    class Meta:
        model = Comment
        fields = ['content']