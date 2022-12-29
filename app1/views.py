from django.shortcuts import render

def first(request):
    d={'name':'venky'}
    return render(request,'first.html',context=d)
