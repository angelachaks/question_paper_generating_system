from django.shortcuts import render

# Create your views here.
def generate_question_paper(request):
    return render(request, 'Questiongeneration/questiongenerator.html', {})

def regenerate(request):
    return render(request, '', {})

def print_paper(request):
    return render(request, '', {})
    
def reject_paper(request):
    return render(request, '', {})

def approve_paper(request):
    return render(request, '', {})

def save_paper(request):
    return render(request, '', {})
