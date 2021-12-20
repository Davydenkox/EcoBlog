from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from apps.post.views import Detalle
from apps.usuarios.models import Usuario
from apps.post.models import Post
from apps.comentario.models import Comentario
from apps.comentario.forms import Comentario as comfor

# Create your views here.
@login_required
def newnota(request):
    if request.method == "POST":
        current_user = request.user
        user = Usuario.objects.get(id=current_user.id)
        model = Comentario
        newnote = comfor(request.POST)
        if newnote.is_valid():
            #print("entro")
            model.autor = newnote.cleaned_data["autor"]
            model.detalle = newnote.cleaned_data["detalle"]
            model.estado = newnote.cleaned_data["estado"]
            grabar = Comentario(detalle=model.detalle, autor=user, estado=model.estado)
            grabar.save()
            return redirect(request)
        else:
            return redirect(request)
    else:
        newnote = comfor()
    return redirect(request)

