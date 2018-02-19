from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import District, Candidate

def index(request):
    district_list = District.objects.all()
    return render(request, "polls/index.html", locals())

def detail(request, id=None):
    district = District.objects.get(id=id)


    return render(request, "polls/detail.html", locals())

def vote(request):
    try:
        if request.POST:

            candidate = Candidate.objects.get(id=request.POST['candidate_id'])
            candidate.no_of_vote += 1
            candidate.save()
    except:
        candidate = None
    return render(request, "polls/vote.html", locals())
