from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    allPosts = Post.objects.all()
    context = {'posts':allPosts}
    return render(request, 'home/home.html',context)
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        contact = Contact(name=name,email=email,phone=phone,content=content)
        contact.save()
        messages.success(request,'Thank You for your Response. We will get back to you soon.')
    return render(request,'home/contact.html')
def about(request):
    return render(request,'home/about.html')
def search(request):
    query = request.GET['sey']
    if len(query)>80:
        allPosts = []
        query = ""
    else:
        allPostst = Post.objects.filter(title__icontains=query)
        allPostsc = Post.objects.filter(content__icontains=query)
        allPosts = allPostst.union(allPostsc)
 
    context = {'posts':allPosts,'query':query}
    return render(request,'home/search.html',context)

def signuphandle(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        p1 = request.POST['p1']
        p2 = request.POST['p2']

        if len(name) > 10:
            messages.error(request,"Username should be less than 10 characters")
            return redirect('/')
        if p1!=p2:
            messages.error(request,"Passwords did not match")
            return redirect('/')
        if not name.isalnum():
            messages.error(request, "Username should be alphanumeric")
            return redirect('/')

        myuser = User.objects.create_user(username=name,email=email,password=p1)
        myuser.save()
        messages.success(request,"Your Account has been created successfully")
        return redirect('/')
    else:
        return HttpResponse('404 - Page Not Found')

@login_required
def logouthandle(request):
            logout(request)
            messages.success(request,"Logout successfull")
            return redirect('/')

def loginhandle(request):
    if request.method == 'POST':
        username = request.POST['emaill']
        p1 = request.POST['p1l']

        user = authenticate(username=username,password=p1)

        if user is not None:
            login(request,user)
            messages.success(request,"Login successfull")
            return redirect('/')

        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/')

    else:
        return HttpResponse('404 - Page Not Found')

