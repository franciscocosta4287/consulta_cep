from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render, redirect
from .models import Endereco


def consulta_cep_ok(request):
    if request.method == 'POST':
        cep = request.POST.get('cep')
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                endereco = Endereco.objects.create(
                    cep=cep,
                    logradouro=data.get("logradouro", ""),
                    complemento=data.get("complemento", ""),
                    bairro=data.get("bairro", ""),
                    localidade=data.get("localidade", ""),
                    uf=data.get("uf", ""),
                    ibge=data.get("ibge", ""),
                    gia=data.get("gia", ""),
                    ddd=data.get("ddd", ""),
                    siafi=data.get("siafi", ""),
                )
                endereco.save()
                return redirect('relatorio_cep')
        return render(request, 'ceps/consulta.html', {'error': 'CEP inválido ou não encontrado.'})
    return render(request, 'ceps/consulta.html')



def relatorio_cep(request):
    enderecos = Endereco.objects.all()
    return render(request, 'ceps/relatorio.html', {'enderecos': enderecos})



def consulta_cep_ok(request):
    if request.method == 'POST':
        cep = request.POST.get('cep')
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                # Renderizar os dados para visualização antes de salvar
                return render(request, 'ceps/visualizar.html', {'data': data})
        return render(request, 'ceps/consulta.html', {'error': 'CEP inválido ou não encontrado.'})
    return render(request, 'ceps/consulta.html')

def salvar_cep_ok(request):
    if request.method == 'POST':
        # Captura os dados enviados no formulário
        data = {
            'cep': request.POST.get('cep'),
            'logradouro': request.POST.get('logradouro'),
            'complemento': request.POST.get('complemento'),
            'bairro': request.POST.get('bairro'),
            'localidade': request.POST.get('localidade'),
            'uf': request.POST.get('uf'),
            'ibge': request.POST.get('ibge'),
            'gia': request.POST.get('gia'),
            'ddd': request.POST.get('ddd'),
            'siafi': request.POST.get('siafi'),
        }

        # Salva no banco de dados
        endereco = Endereco.objects.create(**data)
        endereco.save()
        return redirect('relatorio_cep')
    return redirect('consulta_cep')




def dashboard(request):
    return render(request, 'ceps/dashboard.html')

def consulta_cep(request):
    data = None
    error = None

    if request.method == 'POST':
        cep = request.POST.get('cep')
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if response.status_code == 200:
            data = response.json()
            if "erro" in data:
                error = "CEP não encontrado."
        else:
            error = "Erro ao consultar o CEP."

    return render(request, 'ceps/consulta.html', {'data': data, 'error': error})

def salvar_cep(request):
    if request.method == 'POST':
        # Captura os dados enviados no formulário
        data = {
            'cep': request.POST.get('cep'),
            'logradouro': request.POST.get('logradouro'),
            'complemento': request.POST.get('complemento'),
            'bairro': request.POST.get('bairro'),
            'localidade': request.POST.get('localidade'),
            'uf': request.POST.get('uf'),
            'ibge': request.POST.get('ibge'),
            'gia': request.POST.get('gia'),
            'ddd': request.POST.get('ddd'),
            'siafi': request.POST.get('siafi'),
            'numero': request.POST.get('numero'),
        }

        # Salva no banco de dados
        Endereco.objects.create(**data)
        return redirect('relatorio_cep')

    return redirect('consulta_cep')


# =AJAX===============================
import requests
from django.http import JsonResponse

def consulta_cep_ajax(request):
    if request.method == 'GET':
        cep = request.GET.get('cep')
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if response.status_code == 200:
            data = response.json()
            if "erro" in data:
                return JsonResponse({'error': 'CEP não encontrado.'}, status=404)
            return JsonResponse(data)
        return JsonResponse({'error': 'Erro ao consultar o CEP.'}, status=400)
