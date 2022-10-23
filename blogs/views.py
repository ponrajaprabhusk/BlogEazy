from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import urls, forms 
from .forms import BlogForm
from .models import Blog

# Create your views here.
def allBlogs(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}

    return render(request, 'main.html', context)

@login_required(login_url='login')
def createBlog(request):
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('')

    context = {'form':form}

    return render(request, 'create_blog.html', context) 

@login_required(login_url='login')
def editBlog(request,pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('')


    context = {'form': form, 'blog': blog}
    return render(request, "edit_blog.html", context)

@login_required(login_url='login')
def deleteBlog(request,pk):
    blog = Blog.objects.get(id=pk)

    if request.method == 'POST':
        blog.delete()
        return redirect('')

    
    context = {'blog': blog}
    return render(request, "delete_blog.html", context)
