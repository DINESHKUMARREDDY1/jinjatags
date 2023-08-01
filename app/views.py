from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'a':100, 'b': 20,'c':30}
    return render(request,'data_render.html',context=d)
def condition1(request):
    d={'games':['cricket','football']}
    return render(request,'condition1.html',context=d)