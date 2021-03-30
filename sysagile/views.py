from django.shortcuts import render, redirect
from . models import Contact, User
# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        msg = "Message saved succesfully"
        return render(request, 'contact.html', {'msg': msg})
    else:
        return render(request, 'contact.html')


def signup(request):
    if request.method == "POST":
        try:
            username = User.objects.get(username=request.POST['username'])
            msg = "User Name Is Already Taken"
            return render(request, 'signup.html', {'msg': msg})

        except:

            try:
                user = User.objects.get(email=request.POST['email'])
                msg = "Email already Registered"
                return render(request, 'signup.html', {'msg': msg})
            except:
                if request.POST['password'] == request.POST['confirmpassword']:
                    User.objects.create(
                        username=request.POST['username'],
                        name=request.POST['name'],
                        email=request.POST['email'],
                        password=request.POST['password'],
                        confirmpassword=request.POST['confirmpassword']
                    )
                    msg = "Registration Completed Succesfully"
                    return render(request, 'login.html', {'msg': msg})
                else:
                    msg = "Password Doesn't match"
                    return render(request, 'signup.html', {'msg': msg})

    else:
        return render(request, 'signup.html')


def login(request):

    if request.method == "POST":
        try:
            user = User.objects.get(
                email=request.POST['email'],
                password=request.POST['password']
            )
            if user:
                request.session['name'] = user.name
                request.session['email'] = user.email
                return render(request, 'index.html')

        except:
            msg = "Password Doesn't matched"
            return render(request, 'login.html', {'msg': msg})
    else:
        return render(request, "login.html")


def logout(request):
    try:
        del request.session['email']
        del request.session['name']
        return render(request, 'login.html')
    except:
        return render(request, 'index.html')


def change_password(request):
    if request.method == "POST":
        user = User.objects.get(email=request.session['email'])
        if user.password == request.POST['Old_Password']:
            if request.POST['New_Password'] == request.POST['Confirm_New_Password']:
                user.password = request.POST['New_Password']
                user.confirmpassword = request.POST['Confirm_New_Password']
                user.save()
                return redirect('logout')
            else:
                msg = "New Password & Confirm New Password Doesn't Matched"
                return render(request, 'change_password.html', {'msg': msg})
        else:
            msg = "Old Password is Incorrect"
            return render(request, 'change_password.html', {'msg': msg})
    else:
        return render(request, 'change_password.html')
