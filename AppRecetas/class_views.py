from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recetas
from django.core.paginator import Paginator

##ver/listar las recetas
## ver si lo listo con un for 

class RecetaListView (ListView):
    model = Recetas
    template_name = "AppRecetas/recetas_list.html"
    paginate_by = 6  # 6 recetas por página

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recetas_list = context['object_list']
        paginator = Paginator(recetas_list, self.paginate_by)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        return context

##acceder al detalle de una receta
class RecetaDetailView (DetailView):
    model = Recetas
    template_name = "AppRecetas/recetas_detalle.html"
    context_object_name = 'receta'

##crear recetas
class RecetaCreateView (CreateView):
    model = Recetas
    success_url = "/AppRecetas/curso-list" #cuando se cree el modelo se dirige acá
    fields = ["nombre","camada"]
    template_name = "AppRecetas/cursos_create.html"  #llama al html para agregar un nuevo curso

##actualizar recetas
class RecetaUpdateView (UpdateView):
    model = Recetas
    success_url = "/AppUNR/curso-list" #cuando se actualice el modelo se dirige acá
    fields = ["nombre"]
    template_name = "AppUNR/cursos_form.html" ##asi se llama el html al que quiero ir

##eliminar recetas
class RecetaDeleteView (DeleteView):
    model = Recetas
    success_url = "/AppUNR/curso-list" #cuando se elimine el modelo se dirige acá
    template_name = "AppUNR/cursos_confirm_delete.html" ##asi se llama el html al que quiero ir