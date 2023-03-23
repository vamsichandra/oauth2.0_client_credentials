from django.shortcuts import render
from django.template import loader
from rest_framework.response import Response
# Create your views here.
# server/views.py
import datetime
import json
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from oauth2_provider.views.generic import ProtectedResourceView
from oauth2_provider.models import AccessToken
from django.utils.decorators import method_decorator
from oauth2_provider.decorators import protected_resource
from oauth2_provider.models import Application
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.decorators import protected_resource
import ast
import requests
from rest_framework.decorators import api_view
from .models import Greeting



def client_credentials(request):

    access_token = AccessToken.objects.create(
        scope='read write',
        expires=datetime.datetime.now() + datetime.timedelta(hours=1),
        token='SOME_CLIENT_CREDENTIALS_TOKEN',
        application=Application.objects.get(client_id='5lTNArDIhesgk6OIIdQiHAl4RIQlLPRF74oUrTqg'),
        user=None
    )
    return JsonResponse({'access_token': access_token.token})




@csrf_exempt
@protected_resource()
def MyProtectedView(request):
    if request.method == 'POST':
       greeting = request.POST.get('greeting')
       print(request)
       print(greeting)
       #serliazer=serliazers.GreatingSerializers(data=greeting)
         
       #logger.info(greeting)
       Greeting.objects.create(text=greeting)
       # if serializer.is_valid():
       #     serializer.save()
            
       if greeting == 'hello':
       #response = requests.post('http://localhost:8000/original_greeting/', data={'greeting': 'goodbye'})
          #return JsonResponse(response.json())
          return JsonResponse({'status': 'hello'})
       else:
          return JsonResponse({'status': 'ok'})  #status=status.HTTP_200_OK
    else:
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



def get_access_token(request):
    url = 'http://localhost:8000/o/token/'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cache-Control': 'no-cache'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': '5lTNArDIhesgk6OIIdQiHAl4RIQlLPRF74oUrTqg',
        'client_secret': 'pbkdf2_sha256$320000$IUUBY1FaYeJl9oN1Ps6N2J$KL5A1/8++18WN06+pONdIqg9nI49bIhJ0eqR95NWauE='
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get('access_token')
#     tt=response.json().get('access_token')
#     print(tt)
#     return JsonResponse(tt,safe=False)




# @api_view(['GET', 'POST'])
def access_protected_view(request):
    url = 'http://localhost:8000/protected-view/'
    # response1 = requests.get(client_credentials(request))
    # resx=response1.json().get('access_token')
    #print(resx)
    tt=get_access_token(request)
    print("this is from tt",tt)
    headers = {
        'Authorization': f'Bearer {tt}'
    }
    #response = requests.post(url, headers=headers)
    data = {
        'greeting': 'hello'
        
    }
    json_data = json.dumps(data)
    response = requests.post(url, headers=headers, data=data)
    print("this i sthe op",response.text)
    tet = response.text


    start_index = tet.find("{")
    end_index = tet.rfind("}") + 1
    json_str = tet[start_index:end_index]


    dictionary = ast.literal_eval(json_str)
    return JsonResponse(dictionary)


