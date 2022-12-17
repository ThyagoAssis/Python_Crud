from django.shortcuts import render, redirect
from .models import Receitas

# Create your views here.
def home(request):
    receitas = Receitas.objects.all()
    return render(request, "index.html", {"receitas": receitas})

def save(request):
    img = request.POST.get("img")
    title = request.POST.get("title")
    description = request.POST.get("description")
    Receitas.objects.create(img=img,title=title,description=description)
    receitas = Receitas.objects.all()
    return render(request, "index.html", {"receitas": receitas})

def editar(request, id):
    receita = Receitas.objects.get(id=id)
    return render(request, 'update.html', {"receita":receita})

def update(request, id):
    img = request.POST.get("img")
    title = request.POST.get("title")
    description = request.POST.get("description")
    receita = Receitas.objects.get(id=id)
    receita.img = img
    receita.title = title
    receita.description = description
    receita.save()
    return redirect(home)

def delete(request, id):
    receita = Receitas.objects.get(id=id)
    receita.delete()
    return redirect(home)
