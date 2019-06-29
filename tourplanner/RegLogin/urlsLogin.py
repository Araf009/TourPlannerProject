from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("homepage/", views.login_validation, name="login_validation")
    #path('<int:album_id>/', views.detail, name='detail')
]