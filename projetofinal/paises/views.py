from django.shortcuts import render
from .models import Pais, Idioma 
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
    success_url = reverse_lazy('lista_pais')

    def form_valid(self, form):
        nome_oficial = form.cleaned_data['nome_oficial'].replace("-", "").strip() 
        url = f"https://restcountries.com/v3.1/name/{nome_oficial}" 
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data:
                pais_info = data[0]

                idiomas = pais_info.get("languages", {})
                idioma_nome = list(idiomas.values())[0] 
                nome_comum = pais_info.get("name", {}).get("common")


                idioma_obj, _ = Idioma.objects.get_or_create(nome=idioma_nome)

                pais_obj, created = Pais.objects.update_or_create(
                nome_oficial=nome_comum,
                defaults={
                    "nome_oficial": pais_info.get("name", {}).get("official"),
                    "capital": pais_info.get("capital", ["Desconhecida"])[0],
                    "regiao": pais_info.get("region", "Desconhecida"),
                    "subregiao": pais_info.get("subregion", "Desconhecida"),
                    "idioma": idioma_obj,
                    "populacao": pais_info.get("population", 0),
                    "area": pais_info.get("area", 0.0)
                }
            )
            else:
                form.add_error("nome_oficial", "País não encontrado pela API do REST Countries.")
                return self.form_invalid(form)
        else:
            form.add_error("nome_oficial", "Erro ao consultar a API.")
            return self.form_invalid(form)

        return super().form_valid(form)

    
class PaisDetailView(DetailView):
    model = Pais
    template_name = 'crud/paisdetail.html'
    context_object_name = 'paises'

class PaisDeleteView(DeleteView):
    model = Pais
    template_name = 'crud/paisdelete.html'
    success_url = reverse_lazy('lista_pais')