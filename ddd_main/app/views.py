from django.shortcuts import render

# inicio
def inicio(request):
    return render(request, 'app/1_inicio.html')

# institucional
def institucional(request):
    return render(request, 'app/2_institucional.html')

# programas e projetos
def programas_projetos(request):
    return render(request, 'app/3_programasProjetos.html')

# transparencia
def transparencia(request):
    return render(request, 'app/4_transparencia.html')

# seja voluntario
def seja_voluntario(request):
    return render(request, 'app/5_sejaVoluntario.html')

#loja
def loja(request):
    return render(request, 'app/6_loja.html')

#patrocinio
def patrocinio(request):
    return render(request, 'app/7_patrocinio.html')

# fale conosco
def fale_conosco(request):
    return render(request, 'app/8_faleConosco.html')

def apoie(request):
    return render(request, 'app/9_apoie.html')
# Create your views here.

