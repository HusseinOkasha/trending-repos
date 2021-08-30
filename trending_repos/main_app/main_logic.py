
from django.http import HttpResponse, HttpResponseRedirect
import datetime
import requests, json
from . import views
    
def index(request):
    date = datetime.datetime.now().date()
    url = f'''https://api.github.com/search/repositories?q=created&:%3E{date}&sort=stars&order=desc&per_page=100'''
    res = requests.get(url).json()
    repos = res["items"] # list of 100 repos each repo has a dict.
    lang_repo={} # language ---> repos using it
    for repo in repos:
        language = repo["language"]
        if language in lang_repo:
            lang_repo[language].append(repo["name"])
        else:
            lang_repo[language]= [repo["name"]]
    context = {"lang_repo":lang_repo}
    return views.index(request, context )
    