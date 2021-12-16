from django.contrib      import admin
from django.contrib.auth import views as auth_views
from django.urls         import path, include 
from apps.usuarios.views import Registrarme


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.inicio, name="inicio"),
    path('', views.Inicio.as_view(), name="inicio"),

    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.logout_then_login, name="logout"),
    path("Registrarme/", Registrarme.as_view(), name="Registrarme"),


    # Includes
    path("Post/", include('apps.post.urls')),
    path("Usuario/", include('apps.usuarios.urls'))
]
