from django.shortcuts import render

# Create your views here.
def quick_look(request):
    return render(request, 'fun_templates/quick_look.html')