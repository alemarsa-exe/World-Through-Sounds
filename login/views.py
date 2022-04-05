import json
from django.http import JsonResponse, StreamingHttpResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


@csrf_exempt
def index(request):
    if request.method == 'POST':
        
        strJson = (request.body).decode()
        print(strJson)
        jsonUser = json.loads(strJson)
        user = authenticate(request, username=jsonUser['name'], password = jsonUser['pswd'])
        
        if user is not None:
            #Success
            login(request, user)
            print("Success")
            return JsonResponse(jsonUser)
        else:
            #Bad login
            print("NOT Success")
            jsonUser = {"userId":0,"role":"","name":"Error","pswd":""}
            return JsonResponse(jsonUser)
        
    else:
        return HttpResponse("Hello, world. You're at the login index.")
    

   