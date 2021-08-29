# Trending-repos
It's a simple API that integrate with GitHub through the following end point.
```code
https://api.github.com/search/repositories?q=created&:%3E{date}&sort=stars&order=desc&per_page=100
```
which return a json containing first 100 trending repos on github, then I return a html page containg
a list of languagues and for each language a list of repos names  which uses that langauge.  
**Warning:** "The secret key in /trending_repos/settings.py" isn't hidden.
