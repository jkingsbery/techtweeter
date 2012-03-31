from django.http import Http404, HttpResponse
import datetime
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

from AlgoTools.objects.PSql import PSql
from django import forms

from random import random as rnd

def index(request):
    things=["The Cloud","Agile","Social","Hyper-local","Scrum","Marketing Technology","Big Data","UX","SOA","SaaS"]
    old_things=["EJB","CORBA"]
    x=int(rnd()*len(things))
    thing1=things[x]
    del things[x]
    thing2=things[int(rnd()*len(things))]
    tweet="When will {0} and {1} intersect?".format(thing1,thing2)
    other_tweet="When Will {0} go the way of {1}?".format(thing1,old_things[int(rnd()*len(old_things))])
    return HttpResponse(tweet + "<br/>" + other_tweet)
