import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # This is similar to ones we have done before. Instead of keeping
    # the HTML / template in a separate directory, we just reply with
    # the HTML embedded here.
    return HttpResponse('''
        <h1>Welcome to my home page!</h1>
        <a href="/about-me">About me</a> <br />
        <a href="/github-api-example">See my GitHub contributions</a> <br />
        <a href="/real_index">real_index</a> <br />
        <a href="/projects">projects</a> <br />
    ''')

def real_index(request):
    content_html = open("content/index.md").read()
    context = {
    "content": content_html,
    }
    return render(request, "base.html", context)

def about_me(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    content_html = open("content/about.md").read()
    context = {
    "content": content_html,
    }
    return render(request, "base.html", context)

def projects(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    content_html = open("content/projects.md").read()
    context = {
    "content": content_html,
    }
    return render(request, "base.html", context)

def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/janeqhacker/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

