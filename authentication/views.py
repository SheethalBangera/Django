import re

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model


def home(request):
    return render(request, "authentication/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        # if User.objects.filter(username=username):
        #     messages.error(request, "Username already exist! Please try some other username.")
        #     return redirect('signin')
        #
        # if User.objects.filter(email=email).exists():
        #     messages.error(request, "Email Already Registered!!")
        #     return redirect('signin')

        try:
            if User.objects.get(username=username):
                messages.info(request, "UserName Is Taken")
                return redirect('signup')
        except:
            pass


        try:
            if User.objects.get(email=email):
                messages.info(request, "Email id Is Taken")
                return redirect('signup')
        except:
            pass
            


        if len(username) < 8:
            messages.error(request, "Username must be of minimum 8 characters!!")
            return redirect('signup')

        if username.isalpha():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')

        def validate_password(password):
            # regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
            if len(password) < 10:
                messages.error(request, "Password should be of minimum 10 characters")
                return True
            if not re.search("[a-z]", password):
                messages.error(request, "Password should include atleast 1 lowercase character")
                return True
            if not re.search("[A-Z]", password):
                messages.error(request, "Password should include atleast 1 uppercase character")
                return True
            if not re.search("[0-9]", password):
                messages.error(request, "Password should include atleast 1 number")
                return True
            if not re.search("[^a-zA-Z0-9]", password):
                messages.error(request, "Password should include atleast 1 special character")
                return True
            # if not regex.search(password) == None:
            #     messages.error(request, "Password should include atleast 1 special character")
            #     return True
            return False

        if validate_password(pass1):
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! ")

        return redirect('signin')

    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/index.html", {"fname": fname})

        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')