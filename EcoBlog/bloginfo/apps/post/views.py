#from django.shortcuts import render

# Create your views here.
from django.http import request
from django.shortcuts          import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls               import reverse_lazy
from django.views.generic      import ListView, CreateView 
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from apps.comentario.forms import ComentarioForm

from apps.comentario.models import Comentario
from .forms  import PostForm
from .models import Post
from apps.usuarios.models import Usuario
from django.shortcuts import redirect, render
#all_users = Usuario.objects.values()

class NuevoComentario(CreateView):
	template_name = "post/comentarios.html"
	model = Comentario
	form_class = ComentarioForm
	#print(get_object_or_404())
	
	def get_success_url(self, **kwargs):
		return reverse_lazy("inicio")
	
	def form_valid(self, form):
		f = form.save(commit=False)
		#all_users = Usuario.objects.values()
		usser= Usuario.objects.get(id=self.request.user.id)
		
		#f.posteo = 
		f.autor = usser
		return super(NuevoComentario, self).form_valid(form)




class ListarAdmin(ListView):
	template_name="post/admin/listar.html"
	model = Post
	context_object_name="post"

	def get_context_data(self, **kwargs):
		context = super(ListarAdmin, self).get_context_data(**kwargs)
		context["nombre_buscado"] = self.request.GET.get("nombre_producto", "")
		return context
	
	def get_queryset(self):
		# self.request
		return Post.objects.all().order_by("id")
	

class NuevoAdmin(CreateView):
	template_name = "post/admin/nuevo.html"
	model = Post
	form_class = PostForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("post:admin_listar")
	
	def form_valid(self, form):
		f = form.save(commit=False)
		f.usuario_id = self.request.user.id
		return super(NuevoAdmin, self).form_valid(form)


class EditarAdmin(UpdateView):
	template_name = "post/admin/editar.html"
	model = Post
	form_class = PostForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("post:admin_listar")
	
class Detalle(DetailView):
	template_name = "post/detalle.html"
	model = Post


class NuevoPost(CreateView):
	template_name = "post/nuevo.html"
	model = Post
	form_class = PostForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("post:admin_listar")
	
	def form_valid(self, form):
		f = form.save(commit=False)
		#all_users = Usuario.objects.values()
		usser= Usuario.objects.get(id=self.request.user.id)

		f.autor = usser
		return super(NuevoPost, self).form_valid(form)
