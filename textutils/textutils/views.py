# I have created this file
# view always return HTTP response

from email.policy import HTTP
from http.client import HTTPResponse
from re import I
from django.http import HttpResponse
from django.shortcuts import render
from string import punctuation

# def hello_world(request):
#     return HttpResponse("<a href=https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7> Django Playlist<a/>")

# render takes 3 arguments 1 --> request (HTTP) 2 --> html file name 3 --> dict
def index(request):
    return render(request, "index.html")
    # return HttpResponse("<h1> HELLO <h1/>")

def analyze(request):
    # get text from index.html textarea tag
    text = request.POST.get("text", "default")
    capitalize = request.POST.get('capitalize', 'off')
    remove_punc = request.POST.get('remove_punc', 'off')
    return_vowels = request.POST.get('return_vowels', 'off')

    params = {"purpose": "Updated String", "analyzed_text": text}
    if capitalize == "on":
        params['analyzed_text'] = params['analyzed_text'].upper()

    if remove_punc == "on":
        for i in punctuation:
            params['analyzed_text'] = params['analyzed_text'].replace(i, "")

    if return_vowels == "on":
        vowels_string = ''
        for i in params['analyzed_text']:
            if i.upper() in 'AEIOU':
                vowels_string += i.upper()
        params['analyzed_text'] = vowels_string

    return render(request, "analyze.html", params)

