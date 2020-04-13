import requests
from django.http import HttpResponse
from django.shortcuts import render
import datetime
import glob
import os

pages = []
all_content_files = glob.glob("content/*.md")
for page in all_content_files:
    file_name = os.path.basename(page)
    name_only, extension = os.path.splitext(file_name)
    pages.append({
        "filename": "content/" + file_name,
        "title": name_only,
        "output": file_name
    })
year = datetime.datetime.now().strftime('%Y')


def index(request):
    content_html = open("content/index.md").read()
    context = {
    "title": "index",
    "content": content_html,
    "year": str(year),
    "pages": pages,
    }
    return render(request, "base.md", context)
    # This is similar to ones we have done before. Instead of keeping
    # the HTML / template in a separate directory, we just reply with
    # the HTML embedded here.
    # return HttpResponse('''
    #     <h1>Welcome to my home page!</h1>
    #     <a href="/about">About me</a> <br />
    #     <a href="/real_index">real_index</a> <br />
    #     <a href="/projects">projects</a> <br />
    #     <a href="/github-api-example">See my GitHub contributions</a> <br />
    # ''')

# def real_index(request):
#     content_html = open("content/index.md").read()
#     context = {
#     "content": content_html,
#     "year": str(year),
#     "pages": pages,
#     }
#     return render(request, "base.md", context)

def about(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    content_html = open("content/about.md").read()
    context = {
    "title": "about",
    "content": content_html,
    "year": str(year),
    "pages": pages,
    }
    return render(request, "base.md", context)

def projects(request):
    content_html = open("content/projects.md").read()
    context = {
    "title": "projects",
    "content": content_html,
    "year": str(year),
    "pages": pages,
    }
    return render(request, "base.md", context)

def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/janeqhacker/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

