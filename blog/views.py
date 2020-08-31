from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post,Comment
from django.contrib import messages
from blog.templatetags import get_dict

# Create your views here.
def bloghome(request):
    allPosts = Post.objects.all()
    context = {'posts':allPosts}
    return render(request, 'blog/blogHome.html',context)
def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    c = Post.objects.filter(slug=slug).count()
    if c == 0:
        return redirect('/blog/')

    comments = Comment.objects.filter(post = post,parent=None)
    replies = Comment.objects.filter(post = post).exclude(parent=None)
    repdict = {}
    for reply in replies:
        if reply.parent.sno not in repdict.keys():
            repdict[reply.parent.sno] = [reply]
        else:
            repdict[reply.parent.sno].append(reply)

    context = {'post':post,'comments':comments,'user':request.user,'replies':repdict}
    return render(request, 'blog/blogPost.html',context)

def comment(request):
    if request.method == 'POST':
        content = request.POST['content']
        user = request.user
        psno = request.POST['psno']
        csno = request.POST['csno']
        post = Post.objects.get(sno=psno)
        if csno == "":
            com = Comment(content=content,user=user,post=post)
            com.save()
            messages.success(request,'Your comment is been added successfully')
        else:
            parent = Comment.objects.get(sno=csno)
            com = Comment(content=content,user=user,post=post,parent=parent)
            com.save()
            messages.success(request,'Your Reply is been added successfully')
        return redirect(f'/blog/{post.slug}')
    else:
        return redirect('/blog/')

  

