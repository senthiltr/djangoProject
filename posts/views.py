from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SignInModel
from .forms import SignInForm
# Create your views here.
def index(request):
    #return HttpResponse('Welcome to Posts Django App')
    
    return render(request, 'posts/index.html')

def signin(request):
    #return HttpResponse('Welcome to Posts Django App')
    if request.method == 'POST':
        userscount = SignInModel.objects.count()
        if userscount == 0:
            new_signin = SignInModel(uname=request.POST['name'], passwd=request.POST['password'])
            new_signin.save()
            return redirect('content')
        else:
            try:
                dd=SignInModel.objects.get(uname=request.POST['name'])
                print("Id:{}, Uname:{}, Password:{}".format(dd.id ,dd.uname ,dd.passwd))
                print(SignInModel.objects.all())
                if dd.uname == request.POST['name']:
                    return redirect('content')
                else:
                    return redirect('')
            except Exception as e:
                print("not exist")
                print(e.message())
                return redirect('index')
            
    form = SignInForm()
    context = {'form':form}
    return render(request, 'posts/signin.html', context)

def content(request):
    #return HttpResponse('Welcome to Posts Django App')
    
    return render(request, 'posts/content.html')