from django.shortcuts import render

# Create your views here.
def home(request):
    context ={}
    return render(request, 'poetries\home.html',context)

def poetry_view(request):
    context ={}
    return render(request, 'poetries\poetry.html',context)

def p_reflections(request):
    context ={'d':'dddddddddddddd'}
    return render(request, 'poetries\p_reflections.html',context)


def i_read_you_view(request):
    context ={}
    return render(request, 'poetries\i_read_you.html',context)

def stories(request):
    context ={}
    return render(request, 'poetries\stories.html',context)

