from django.shortcuts import render
from django.http import HttpRequest, Http404
from . import data
# Create your views here.




def blog(request):

    context = {
   
        'posts': data.posts
    }


    print("posso fazer outras coisasa")
    return render(
        request, 
        'blog/index.html',
        context
        )



def post(request, post_id):
    found_post = None

    for post in data.posts:
        if post['id'] == post_id:
            found_post = post
            break

    
    if found_post is None:
        raise Http404("post nao encontrado")


    context = {
        #'text': 'blog',
        'post': found_post
    }


    return render(
        request, 
        'blog/post.html',
        context
        )



def exemplo(request):
    return render(
        request,
        'blog/exemplo.html',
        {
            'text': 'exemplo'
        }

    )