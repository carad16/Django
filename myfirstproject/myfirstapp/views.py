from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from .forms import *
# Create your views here.
def error_404_view(request,exception):
    return render(request,"404.html")

def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse("About Response")

def add(request,a,b):
    return HttpResponse(a+b)  

def intro(request,name,age):
    mydictionary = {
        "name" : name,
        "age" : age
    }
    return JsonResponse(mydictionary)  

def myfirstpage(request):
    return render(request, "index.html")

def mysecondpage(request):
    return render(request, "sample.html")

def mythirdpage(request):
    var = "hello world"
    greeting = "hey, how are you?"
    fruits = ["apple", "mango", "banana"]
    num1, num2 = 5, 3
    ans = num1 > num2
    mydictionary = {
        "var": var,
        "msg": greeting,
        "myfruits": fruits,
        "num1": num1,
        "num2": num2,
        "ans": ans
    }
    return render(request, "sample1.html",context=mydictionary) 

def myimgpage(request, imgname):
    myimgname = str(imgname)
    myimgname = myimgname.lower()
    print(myimgname)
    if myimgname == "django":
        var =True
    elif myimgname == "python":
        var = False
    mydictionary = {
        "var": var
    }

    return render(request, "imgpage.html", context=mydictionary)

def myform(request): 
    return render(request, "myform.html")

def submitmyform(request):
    mydictionary = {
        "var1" : request.POST['mytext'],
        "var2" : request.POST['mytextarea'],
        "method" : request.method
    }
    return JsonResponse(mydictionary)

def myform1(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
        #    print(title)
        #   print(subject)
        #    var = str("Form Submitted " + str(request.method))
        #    return HttpResponse(var)
        #else:
            mydictionary = {
            "form": FeedbackForm()
        }
            errorflag = False
            Errors = []
            if title != title.upper():
                #mydictionary["error"]=True
                #mydictionary["errormsg"] = "Title should be in Capital"
                #return render(request, "myform1.html", context=mydictionary)
                errorflag = True
                errormsg = "Title should be in Capital"
                Errors.append(errormsg)
            import re
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if not re.search(regex, email):
                errorflag = True
                errormsg = "Not a Valid Email Address"
                Errors.append(errormsg)
            if errorflag != True:
                mydictionary["Success"] = True
                mydictionary["successmsg"] = "Form Submitted"
            mydictionary["error"] = errorflag
            mydictionary["errors"] = Errors
            return render(request, "myform1.html", context=mydictionary)

    elif request.method == "GET":
        form = FeedbackForm()
        mydictionary = {
            "form": form
        }
    return render(request, "myform1.html", context=mydictionary)