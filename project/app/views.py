from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Login page
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            request.session['user']=username
            auth.login(request,user)
            return redirect(index)
        else :
            return redirect(login)
    else:
        return render(request,'login.html')
def logout1(request):
    # if 'user' in request.session:
        # del request.session['user']
        auth.logout(request)
        print(request.user)

        return redirect(index)
    # else:
        return redirect(login)
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        data=User.objects.create_user(username=username,email=email,password=password)
        data.save()
        return redirect(login)
    else:
        return render(request,'register.html')
# pages
def index(request):
    return render(request,'index.html')
def see_all(request):
    return render(request,'see_all.html')
def movie(request):
    return render(request,'movie.html')