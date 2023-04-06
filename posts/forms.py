from django import forms
from .models import Post
POSITION_CHOICES=[
        ('개발', '개발'),
        ('기획', '기획'),
        ('디자인', '디자인'),
]
class PostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': '제목 입력',
                'class' : 'form-control',
                },    
        ),
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={'class': 'form-control'},
        ),
    )
    
    category = forms.ChoiceField( 
        required=True,
        # attrs={'required': True}
        widget=forms.RadioSelect, 
        choices=POSITION_CHOICES,
    )

    class Meta:
        model = Post
        fields = '__all__'