from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
        pass

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'root' and password == 'root':
            request.session['username'] = username
            request.session['is_login'] = True
            return redirect('/index')
        else:
            return render(request, 'login.html')
        pass
    pass

def index(request):
    if request.session['is_login']:
        return HttpResponse(request.session['username'])
    else:
        return HttpResponse('exit')
    pass
