

# Views.py
# I have created this file - Harry
from ast import Param
from os import remove
from string import punctuation
from urllib.request import Request
from django import http
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover= request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    if removepunc == "on":
        analyzed =""
        punctuations = '''""!@#$%^&*()_+}{][<>,.?/'''
        for char in  djtext:
            if  char not in punctuations:
                analyzed = analyzed + char
        Params = {'purpose':'Remove punctutaions','analyzed_text':analyzed}
        return render(request,'analyze.html',Params)
    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        Params ={'purpose':'Change to uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',Params)
    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if  char != "n":
                analyzed = analyzed + char
        Params ={'purpose':'Remoove The Newline','analyzed_text':analyzed}
        return render(request,'analyze.html',Params)
    elif(extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == "" and djtext[index+1]==""):
                analyzed = analyzed+ char
        Params ={'purpose':'Removee The extraline','analyzed_text':analyzed}
        return render(request,'analyze.html',Params) 
    else:
        return HttpResponse("error")





