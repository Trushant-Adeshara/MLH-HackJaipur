from django.shortcuts import render
import pyrebase
from django.contrib import auth
config = {
'apiKey': "AIzaSyDcTmz6t9PYWc4rRXLPCYKgQ3nK6z4OKrg",
'authDomain': "workup-8fb1b.firebaseapp.com",
'databaseURL': "https://workup-8fb1b.firebaseio.com",
'projectId': "workup-8fb1b",
'storageBucket': "workup-8fb1b.appspot.com",
'messagingSenderId': "1091070362356",
'appId': "1:1091070362356:web:3c8372ee0aaca8578254a1",
'measurementId': "G-KBEMYMNH5D"
}
firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database = firebase.database()
def signIn(request):
    return render(request, "authentication/signIn.html")


def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "invalid credentials"
        return render(request, "authentication/signIn.html", {"messg": message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid']=str(session_id)
    return render(request, "intro/home.html", {"e": email})


def logout(request):
    auth.logout(request)
    return render(request, 'authentication/signIn.html')


def signUp(request):

    return render(request, 'authentication/signup.html')


def postsignup(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    try:
        user = authe.create_user_with_email_and_password(email, passw)
        uid = user['localId']
        data = {"name": name, "status": "1"}
        database.child("users").child(uid).child("details").set(data)
    except:
        message = "Unable to create account try again"
        return render(request, "authentication/signup.html",{"messg":message})


    return render(request, "authentication/signIn.html")

