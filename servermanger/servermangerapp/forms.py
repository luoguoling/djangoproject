#coding:utf-8
from django import forms
from django.contrib.auth.models import User
class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput, required=False)
class UploadFileFormmysql(forms.Form):
    file = forms.FileField(widget=forms.FileInput, required=False)
class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u'用户名',
        error_messages={'required':'请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u'用户名',
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label=u'密码',
        error_messages={'required':u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u'密码',

            }
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u'用户名和密码必填')
        else:
            cleaned_data = super(LoginForm,self).clean()
