from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from apps.post.views import Detalle
from apps.usuarios.models import Usuario
from apps.post.models import Post
from apps.post.forms import PostForm
#from apps.comentario.models import Comentario
#from apps.comentario.forms import Comentario as comfor
from django.views.generic import CreateView
from django.urls               import reverse_lazy

# Create your views here.
