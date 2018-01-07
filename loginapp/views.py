from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
        pass

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        if username == 'root' and password == 'root':
            request.session['username'] = username
            request.session['is_login'] = True
            return redirect('/index')
        else:
            return render(request, 'login.html')
        pass
    pass

def index(request):
    # return HttpResponse('ok')
    if request.session.get('is_login',None):
        # return HttpResponse(request.session['username'])
        return render(request, 'index.html', {'username':request.session['username']})
    else:
        return HttpResponse('exit')
    pass

def logout(request):
    request.session.clear()
    return redirect('/login/')




from django.views.decorators.cache import cache_page

# @cache_page(10)
def cache(request):
    import time
    ctime = time.time()
    return render(request,'cache.html',{'ctime':ctime})





# form表单验证
from django import forms
from django.forms import widgets,fields
class FM(forms.Form):
    username = fields.CharField(
        widget = widgets.Textarea(attrs={'class':'c1'}),
        error_messages={'required':'用户名不能为空。'}
    )
    pwd = fields.CharField(
        widget = widgets.PasswordInput,
        min_length=6,
        max_length=12,
        error_messages={'required':'密码不能为空。','min_length':'密码长度最短为6','max_length':'密码最长为12'}
    )
    email = fields.EmailField(error_messages={'required':'邮箱不能为空。','invalid':'邮箱格式错误'})

def fm(request):
    if request.method == 'GET':
        obj = FM()
        return render(request, 'fm.html',{'obj':obj})

    elif request.method == 'POST':
        obj = FM(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            return render(request, 'fm.html')
            pass
        else:
            print(obj.errors.as_json())
            # print(obj.errors)
            return render(request, 'fm.html',{'obj':obj})
            pass
        return render(request, 'fm.html')

