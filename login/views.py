import json
from django.http import JsonResponse, QueryDict, StreamingHttpResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib import messages
from login.models import User, LevelPlayedScore, TopUserScores
from .forms import RegisterUserForm
from django.contrib.auth.models import User
from django.forms.models import model_to_dict


from django.contrib.auth import logout as auth_logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods



@csrf_exempt
def loginUnity(request):
    if request.method == "POST":
        strJson = (request.body).decode()
        jsonUser = json.loads(strJson)
        username = jsonUser['username']
        password = jsonUser['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Success in Consult")
            jsonUser = {"userId":user.id,"role":user.is_superuser,"username":user.username,"pswd":""}
            return JsonResponse(jsonUser)
        else:
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
def levelPlayed(request):
    if request.method == 'POST':   
        strJson = (request.body).decode()
        jsonInfo = json.loads(strJson)
        levelPlayed = LevelPlayedScore(userId=jsonInfo['userId'], level = jsonInfo['level'], score = jsonInfo['score'], lives = jsonInfo['lives'], duration = jsonInfo['duration'])

        if levelPlayed is not None:
            print("Success in Level Info")
            levelPlayed.save()
            return JsonResponse(jsonInfo)
        else:
            print("No Success in Level Info")
            return JsonResponse(jsonInfo)
    else:
        return HttpResponse("Hello, world. You're at the levelPlayed index.")

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
            return redirect('dashboard')
        else:
            messages.error(request, ('Bad login'))
            print("User does not exist")
            return redirect('login')   
    else:
        return render(request, 'Login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('Logged out'))
    return redirect('index')
    

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

            return redirect('dashboard')
        else:
            print(form.errors)
            return render(request, 'Signup.html', {'form': form})   
    else:
        return render(request, 'Signup.html')   

@csrf_exempt
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard2.0.html')
    else:
        return redirect('login')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'perfil.html')
    else:
        return redirect('login')

@login_required
def remove_account(request):
    if request.method=="POST":
        user_pk = request.user.pk
        auth_logout(request)
        User = get_user_model()
        User.objects.filter(pk=user_pk).delete()
        # …
        # return HTTP response
        print("Se ha eliminado la cuenta")
        return redirect('login')
    else:
        return HttpResponse('No hiciste nada')

@csrf_exempt
def topScores(request): 
    if request.method=="POST":
        strJson = (request.body).decode()
        jsonInfo = json.loads(strJson)
        
        newTopScores = TopUserScores(userId=jsonInfo['userId'],scoreLevel1=jsonInfo['scoreLevel1'],scoreLevel2=jsonInfo['scoreLevel2'],scoreLevel3=jsonInfo['scoreLevel3'],scoreLevel4=jsonInfo['scoreLevel4'])
        topScores = TopUserScores()
        try:
            topScores = TopUserScores.objects.get(userId=jsonInfo['userId'])
            topScores.delete()
        except topScores.DoesNotExist:
            pass

        if newTopScores is not None:
            newTopScores.save()
            print("Succes in TopScores")

            return JsonResponse(jsonInfo)
        else:
            print("Not Succes in TopScores")
            jsonUser = {"userId":0,"role":"","name":"Error","pswd":""}
            return JsonResponse(jsonUser)
    else:
        return HttpResponse('TopScoreViews')

@csrf_exempt
def getTopScore(request): 
    if request.method=="POST":
        strJson = (request.body).decode()
        jsonInfo = json.loads(strJson)

        topScores = TopUserScores()
        try:
            topScores = TopUserScores.objects.get(userId=jsonInfo['userId'])
        except topScores.DoesNotExist:
            print("User Does Not exist yet")
        
        jsonObj = model_to_dict(topScores)
        print(jsonObj)
        return JsonResponse(jsonObj)
    return HttpResponse("getTopScores")
        
