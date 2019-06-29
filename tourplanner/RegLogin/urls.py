from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="front-page"),
    path("1/", views.register_guide, name="register_guide"),
    path("2/", views.register_user, name="register_user"),
    path("guide/", views.guide_registration_data, name="guide_registration_data"),
    path("user/", views.user_registration_data, name="user_registration_data"),
    path("editUser/", views.display_user_edit_page, name="user_edit_page"),
    path("editUserSave/", views.edit_user_save_changes, name = "user_edit_save" )
]