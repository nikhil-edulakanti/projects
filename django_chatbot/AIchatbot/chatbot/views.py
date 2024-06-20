from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone

from .models import chat

import openai


# Create your views here.


openai_api_key="key"
openai.api_key = openai_api_key

def ask_ai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response['choices'][0]['message']['content']
 

def home(request):
    chats=chat.objects.filter(user=request.user)
    if request.method=='POST':
        message= request.POST.get('message')
        response= ask_ai(message)
        chat_history=chat(user=request.user, message=message, response= response, created_at=timezone.now())
        chat_history.save()
        return JsonResponse({'message': message, 'response':response})
    return render(request,'templates/chatbot.html', {"chats":chats})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request, username=username, password=password)   
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            error="Invalid User/Password"
            return render(request, 'templates/login.html', {"error_message":error})     
    else:    
        return render(request, 'templates/login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('home')
            except:
                error="Error creating account"
                return render(request, 'templates/register.html', {"error_message": error})
            
        else:
            error="Passwords don't match"
            return render(request, 'templates/register.html', {'error_message':error})
    return render(request, 'templates/register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
