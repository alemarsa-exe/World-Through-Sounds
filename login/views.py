import json
from django.http import JsonResponse, QueryDict, StreamingHttpResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib import messages
from login.models import User
from .forms import RegisterUserForm


@csrf_exempt
def index(request):
    if request.method == 'POST':
        
        strJson = (request.body).decode()
        print(strJson)
        jsonUser = json.loads(strJson)
        user = User(userId=jsonUser['userId'], role = jsonUser['role'], username=jsonUser['username'], password = jsonUser['password1'])
        existsDb = User.objects.filter(userId = jsonUser['userId'])
        
        if (user is not None and len(existsDb) > 0) and existsDb[0].getPassword() == jsonUser['password1'] and existsDb[0].getUsername() == jsonUser['username']:
            #Success
            print("Success in Consult")
            return JsonResponse(jsonUser)
        else:
            #Bad login
            print("NOT Success in Consult")
            jsonUser = {"userId":0,"role":"","username":"Error","pswd":""}
            return JsonResponse(jsonUser)
        
    else:
        return HttpResponse("Hello, world. You're at the login index.")


@csrf_exempt
def signUp(request):
    if request.method == 'POST':   
        strJson = (request.body).decode()
        jsonUser = json.loads(strJson)
        user = User(userId=jsonUser['userId'], role = jsonUser['role'], username=jsonUser['username'], password = jsonUser['password1'])
        existsDb = User.objects.filter(userId = jsonUser['userId'])

        if len(existsDb) == 0:
            print("Success in Sign Up")
            user.save()
            return JsonResponse(jsonUser)
        else:
            print("User already Exists")
            jsonUser = {"userId":0,"role":"","username":"Error","pswd":""}
            return JsonResponse(jsonUser)
    else:
        return HttpResponse("Hello, world. You're at the Sign Up index.")


@csrf_exempt
def change(request):
    if request.method == 'POST':

        strJson = (request.body).decode()
        jsonUser = json.loads(strJson)
        user = User.objects.get(userId = jsonUser['userId'])
        if user is not None:
            user.changeUsername(jsonUser['username'])
            print("Success in Change")
            user.save()
            return JsonResponse(jsonUser)
        else:
            print("Error in change")
            jsonUser = {"userId":0,"role":"","name":"Error","pswd":""}
            return JsonResponse(jsonUser)
            
    else:
        return HttpResponse("Hello, world. You're at the Change index.")

@csrf_exempt
def contacto(request):
    return render(request, 'contacto.html')

@csrf_exempt
def descarga(request):
    return render(request, 'descarga.html')

@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def leaderboards(request):
    return render(request, 'leaderboards.html')
    
@csrf_exempt
def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('leaderboards')
        else:
            messages.error(request, ('Bad login'))
            print("User does not exist")
            return redirect('login')   
    else:
        return render(request, 'Login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('Logged out'))
    return redirect('Login')
    

@csrf_exempt
def signupUser(request):
    if request.method == 'POST':
        #print(request.POST)
        form = RegisterUserForm(request.POST)
        #print(form)
        #print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, ('Registration seccessful'))

            return redirect('index')
        else:
            print(form.errors)
            return render(request, 'Signup.html', {'form': form})   
    else:
        return render(request, 'Signup.html')   
