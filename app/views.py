from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

from app.models import Students


# Create your views here.
def home(request):
    user=request,User
    students=Students.objects.all()
    return render(request,"home.html",{'username':user,'students':students})

def signuppage(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        pass1=request.POST.get("password")
        pass2=request.POST.get("password2")
        if pass1 == pass2:
            myuser = User.objects.create_user(name,email,pass1)
            myuser.save()
            return redirect("loginpage")
        else:
            return redirect("signuppage")
    return render(request,"signup.html")

def loginpage(request):
    if request.method == "POST":
        name=request.POST.get("name")
        password=request.POST.get("password")
        user = authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect("homepage")
        else:
            return redirect("loginpage")
    return render(request,"login.html")

def addpage(request):
    if request.method=="POST":
        name=request.POST.get("name")
        semster=request.POST.get("semester")
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        image = request.FILES.get("imagefile")
        
        print(image)
        students=Students(
            name=name,
            semester=semster,
            address=address,
            phone=phone,
            proimg = image,
        )
        students.save()
        return redirect("homepage")
    return render(request,"home.html")

def updatepage(request,id):
    if request.method=="POST":
        name=request.POST.get("name")
        semster=request.POST.get("semester")
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        image = request.FILES.get("imagefile")
        
        print(image)
        students=Students(
            id=id,
            name=name,
            semester=semster,
            address=address,
            phone=phone,
            proimg = image,
        )
        students.save()
        return redirect("homepage")
    return render(request,"home.html")

def deletepage(request,id):
    students=Students.objects.get(id=id)
    students.delete()
    return redirect("homepage")

def logoutpage(request):
    logout(request)
    return redirect("loginpage")