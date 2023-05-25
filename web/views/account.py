from django.shortcuts import render, HttpResponse, redirect
from web.models import *
from django import forms
from io import BytesIO

from system.utils.plugins import Pagination, md5, check_code
# Create your views here.

class LoginForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '这里填写用户名喵~'})
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '这里填写密码喵~'})
    )
    code_str = forms.CharField(
        label='图片验证码',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '这里填写验证码喵~'})
    )

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

def login(request):
    if request.method == 'GET':
        formset = LoginForm
        return render(request, 'login.html', {'formset': formset})

    formset = LoginForm(data=request.POST)
    if formset.is_valid():
        user_code_input = formset.cleaned_data.pop('code_str')
        if user_code_input.upper() != request.session.get('image_code', '').upper():
            formset.add_error('code_str', '错误（先校验验证码）')
            return render(request, 'login.html', {'formset': formset})

        user_object = User.objects.filter(**formset.cleaned_data).first()
        if user_object:
            request.session['info'] = {'id': user_object.id, 'username': user_object.username}
            request.session.set_expiry(60 * 60)

            return redirect('/material/list/')
        else:
            formset.add_error('password', '发生错误了，再试试看~')
            return render(request, 'login.html', {'formset': formset})
    else:
        return render(request, 'login.html', {'formset': formset})


def img_code(request):
    img, code_str = check_code()
    # print(code_str)

    request.session['image_code'] = code_str
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, format='png')

    return HttpResponse(stream.getvalue())

def logout(request):
    request.session.clear()
    return redirect('/')

def homepage(request):

    return render(request, 'style.html')