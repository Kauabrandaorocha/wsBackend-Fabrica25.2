from django.shortcuts import render
from .models import Pais 
from .forms import PaisForm
from django.views.generic import FormView, DetailView, DeleteView, ListView
from django.urls import reverse_lazy
import requests

# Create your views here.
def base(request):
    return render(request, 'entrada.html')

class PaisListView(ListView):
    model = Pais
    template_name = 'crud/paislist.html'
    context_object_name = 'paises'

class PaisFormView(FormView):
    template_name = 'crud/paisform.html'
    form_class = PaisForm
    success_url = reverse_lazy('listar_pais')

    def form_valid(self, form):
        nome_oficial = form.cleaned_data['nome_oficial'].replace("-", "").strip() 
        url = f"https://restcountries.com/v3.1/name/{nome_oficial}" 
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                pais_obj, created = Pais.objects.update_or_create(
                    nome_oficial=nome_oficial,
                    defaults={
                        "nome_oficial": data.get("nome_oficial"),
                        "capital": data.get("capital"), 
                        "regiao": data.get("regiao"), 
                        "subregiao": data.get("subregiao"), 
                        "idioma": data.get("idioma"), 
                        "populacao": data.get("populacao"), 
                        "area": data.get("area")
                    }
                )
            else:
                form.add_error("nome_oficial", "País não encontrado pela API do REST Countries.")
                return self.form_invalid(form)

        else:
            form.add_error("nome_oficial", "Nome do país não encontrado.")

        return super().form_valid(form)
    
class PaisDetailView(DetailView):
    model = Pais
    template_name = 'crud/paisdetail.html'
    context_object_name = 'paises'

class PaisDeleteView(DeleteView):
    model = Pais
    template_name = 'crud/paisdelete.html'
    success_url = reverse_lazy('listar_pais')