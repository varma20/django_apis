from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['POST'])

def login_view_with_post(request):

    try:

        username = request.data.get("username")
        password = request.data.get("password")
        auth_user = authenticate(request,username=username,password=password)

        if User.objects.filter(username=username).exists() and auth_user:

            user = User.objects.get(username=username)
            token, created = Token.objects.get_or_create(user=user)

            response = {
                'message' : "Login Successful",

                'token' : token.key
            }

            return Response(response,status=200)

        else:
            return Response({'error':"Invalid Credentials"},status=200)

    except Exception as e:
        return Response({'error':"Invalid Credentials"},status=200)

@api_view(['POST'])

def logout_view_with_post(request):

    try:

        user_token = request.data.get("user_token")
        token = Token.objects.get(key = user_token)
        token.delete()
        return Response({"Message":"Logged Out"},status = 200)

    except Exception as e:
        return Response({'error':"Logged Out"},status=200)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect('home/')
        else:
            redirect('login/')

    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    return render(request,'accounts/logout.html')

def home_view(request):
    return render(request,'accounts/home.html')
