from django.urls import path
from .import views

urlpatterns = [
    path('',views.home_view, name = "home"),
    path('create/',views.product_create_view, name = "product_create"),
    path('list/ ',views.product_list_view, name = "product_list"),
    path('update/<product_id>/',views.product_update_view, name = "product_update"),
    path('delete/<product_id>/',views.product_delete_view, name = "product_delete"),
]