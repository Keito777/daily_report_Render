from django import forms
from django.contrib.auth.forms import AuthenticationForm 

#signup
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from .models import CustomUser

# password
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm

class LoginForm(AuthenticationForm):
    """ログオンフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


'''サインアップ用フォーム'''
class SignupForm(UserCreationForm):

    '''UserCreationFormのフィールド'''
    # CustomUserモデルのフィールドとは別でフォームに表示される
    # password1 = forms.~
    # password2 = forms.~ （確認用）

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

'''ユーザー情報更新用フォーム'''
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    # bootstrap4対応
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = '' # 全フィールドを入力必須

'''パスワード変更フォーム'''
class MyPasswordChangeForm(PasswordChangeForm):

    # bootstrap4対応で、classを指定
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'