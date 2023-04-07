from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model
from django.forms.widgets import DateInput

#회원가입폼
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label = '아이디')
    email = forms.EmailField(label = '이메일')
    birthday = forms.DateField(
        label = '생년월일',
        widget= DateInput(attrs = {'type' : 'date'})     
    )

    class Meta:
        model = get_user_model()
        fields = ('username','email','first_name','last_name','password1','password2','birthday')

#회원수정폼
class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(label = '이메일')
    birthday = forms.DateField(
        label = '생년월일',
        widget= DateInput(attrs = {'type' : 'date'})     
    )

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email','first_name','last_name','birthday')

# #회원조회폼
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username','email','first_name','last_name','birthday')