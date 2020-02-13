
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    # return render(request,'home.html',{'Name':'Tejinder'})
    return render(request,'home.html')
# def Teji(request):
    # return HttpResponse('<h1>Tejinder Pal Singh</h1>')
def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictonary = {}
    for word in wordlist:
        if word in worddictonary:
            #increment
            worddictonary[word] +=1
        else:
            #add to the dictionary
            worddictonary[word] =1

    sortedwords = sorted(worddictonary.items() , key=operator.itemgetter(1), reverse=True)


    # print(fulltext)
    # return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddictonary':worddictonary.items()})
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

def about(request):
    # return render(request,'home.html',{'Name':'Tejinder'})
    return render(request,'about.html')
