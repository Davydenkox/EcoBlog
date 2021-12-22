from django.urls import path 

from ..post import views


app_name = "post"

urlpatterns = [
	#path("Detalle/", views.detalle, name="detalle"),
	path("Detalle/<int:pk>/", views.Detalle.as_view(), name="detalle"),
	path("Detalle/<int:pk>/comentarios", views.NuevoComentario.as_view(), name="comentarios"),
	path("Detalle/<int:pk>/vercomentarios", views.VerComentario.as_view(), name="vercomentarios"),

	#path("Detalle/<int:pk>/", views.detalle1, name="detalle_pk"),
	
	# Admin
	#path("Admin/Listar/", views.ListarAdmin.as_view(), name="admin_listar"),
	path("Admin/Nuevo/", views.NuevoAdmin.as_view(), name="admin_nuevo"),
	path("Admin/Editar/<int:pk>/", views.EditarAdmin.as_view(), name="admin_editar"),
	path("nuevo/", views.NuevoPost.as_view(), name="nuevoPost"),

]