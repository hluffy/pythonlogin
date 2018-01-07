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
