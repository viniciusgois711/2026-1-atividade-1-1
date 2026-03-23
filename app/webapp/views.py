from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Professor! Sou seu aluno Lucas Vinícius em SO!")