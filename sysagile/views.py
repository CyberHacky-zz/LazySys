from django.shortcuts import render, redirect
from . models import Contact, User
# Create your views here.


def index(request):

    try:

        if request.session['email']:

            return render(request, 'index.html')
    except Exception as e:
        print(e)
        print("Except Called")
        return render(request, 'login.html')


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
                return render(request, 'index.html', {'user': user})

        except Exception as e:
            print(e)
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
                return render(request, 'profile.html', {'msg': msg})
        else:
            msg = "Old Password is Incorrect"
            return render(request, 'profile.html', {'msg': msg})
    else:
        return render(request, 'profile.html')


def update_profile(request):
    user = User.objects.get(email=request.session['email'])
    user.username = request.POST['username']
    user.name = request.POST['name']
    try:
        User.objects.get(email=request.POST['email'])
        msg = "Email is already used"
        return render(request, 'profile.html', {'msg': msg, 'user': user})
    except:
        user.email = request.POST['email']
    user.save()
    msg = "Data Updated Succesfully"
    return render(request, 'profile.html', {'msg': msg, 'user': user})


def profile(request):
    user = User.objects.get(email=request.session['email'])

    return render(request, 'profile.html', {'user': user})


def forgot_password(request):

    return render(request, 'forgot_password.html')


# Client - Server configuration

def client(request):
    user = User.objects.get(email=request.session['email'])
    return render(request, 'client.html', {'user': user})


def server(request):
    user = User.objects.get(email=request.session['email'])
    return render(request, 'server.html', {'user': user})


def terminal(request):
    user = User.objects.get(email=request.session['email'])
    return render(request, 'terminal.html', {'user': user})


def dashboard(request):
    user = User.objects.get(email=request.session['email'])
    return render(request, 'dashboard.html', {'user': user})
