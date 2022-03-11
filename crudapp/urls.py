from django.urls import path

from crudapp import views

app_name = 'shop'
urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('retrive/<int:prod_id>', views.retrive, name='retrive'),
    path('update/<int:prod_id>', views.update, name='update'),
    path('delete/<int:prod_id>', views.delete, name='delete'),
]
