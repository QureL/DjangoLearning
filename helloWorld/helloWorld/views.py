from django.shortcuts import render
 
def run(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'run.html', context)
