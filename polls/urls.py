from django.conf.urls import url

from . import views

# The url() function is passed four arguments, two required: regex and view, and two optional: kwargs, and name.

# regex (regular expression): https://docs.djangoproject.com/en/1.8/intro/tutorial03/#url-argument-regex
# view (function): https://docs.djangoproject.com/en/1.8/intro/tutorial03/#url-argument-view
# kwargs (keyword arguments): https://docs.djangoproject.com/en/1.8/intro/tutorial03/#url-argument-kwargs
# name (URL naming): https://docs.djangoproject.com/en/1.8/intro/tutorial03/#url-argument-name

# The 'name' value is retrieved from ./polls/views.py

# To get from a URL to a view, Django uses what are known as 'URLconfs'.
# A URLconf maps URL patterns (described as regular expressions) to views.

# v1.0: Original concept, hard-coded URL
# urlpatterns = [
#     # ex: /polls/
#     url(r'^$', views.index, name='index'),
#     # ?P<question_id> defines the name that will be used to identify the matched pattern
#     # [0-9]+ is a regular expression to match a sequence of digits (i.e., a number)
#     # ex: /polls/5/
#     # the 'name' value as called by the {% url %} template tag
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]

# v2.0: Generic view
# SEE: https://docs.djangoproject.com/en/1.8/intro/tutorial04/#amend-urlconf
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
