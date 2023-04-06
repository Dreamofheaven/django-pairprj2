from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model

#회원가입폼
class CustomUserCreationForm(UserCreationForm):
    id = forms.CharField(
        label="아이디", 
        required=True, 
        max_length=30, 
    )
    email = forms.EmailField(
        label = "이메일",
        required=False,
    )

    class Meta:
        model = get_user_model()
        fields = ('id','email','first_name','last_name','password1','password2')

#회원수정폼
class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email','first_name','last_name')
