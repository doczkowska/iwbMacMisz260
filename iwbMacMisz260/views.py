from django.http.response import HttpResponse
from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from service.forms import CreateUserForm
from django.core.mail import EmailMessage
from django.conf import settings

def hello():
    return HttpResponse("""<html>
    <body>
        <b>Witaj świecie!!!</b>
        <div>{}</div>
    </body>
</html>""".format(datetime.today()))
    


def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data.get("username"),
                                password=form.cleaned_data.get("password1"))
            login(request=request,
                  user=user)
            
            email = EmailMessage(
                'Potwierdzenie Rejestracji',
                'Dziękuję to był tylko test',
                settings.EMAIL_HOST_USER,
                [request.owner.email])
            
            email.fail_silently = False
            email.send()  
            print('Wysłano Mail na: ',request.owner.email)      
            return redirect("startpage")

    else:
        form = CreateUserForm()
    return render(request,
                  template_name="signup.html",
                  context={"form": form},)

def startpage(request):
    return render(request,
                  template_name= "service/start.html")

def profile(request):
    return render(request,
                  template_name= "service/profile.html")
