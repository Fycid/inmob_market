from django.urls         import path
from .                   import views

app_name = "usuario"

urlpatterns = [
    path('Registrarme/', views.Registrarme.as_view(), name = "registrarme"),
    path('Listado/', views.ListarUser.as_view(), name = "listar"),
    path('Eliminar/<int:pk>/',views.BorrarUser.as_view(), name = "elimina"),
     path("Editar/<int:pk>/", views.EditarUser.as_view(), name = "editar"),

    

  

]