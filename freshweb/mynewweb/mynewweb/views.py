from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):

    return render(request,'index.html',{'key1':'i am coming from to python code'})


def result(request):
    article=request.GET['article']
    words=article.split()
    word_count=len(words)
    dict_words= {}

    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1

    var_dict=sorted(dict_words.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'result.html',{'article':article,'word_count':word_count,'dict_words':var_dict})

