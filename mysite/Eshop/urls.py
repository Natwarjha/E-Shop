from django.urls import path, include
from Eshop import views

app_name='Eshop'

urlpatterns = [

    
    # Function based home view.
    # --------------------------------------------------------------------------------
    path('home/', views.index, name= 'index'),

    
    # Function based detail view.
    # --------------------------------------------------------------------------------
    path('detail/<int:item_id>/', views.detail, name='detail'),

    
    # Function based create_item view.
    # --------------------------------------------------------------------------------
    path('add/', views.create_item, name='create_item'),

    
    # Function based update_item view.
    # --------------------------------------------------------------------------------
    path('update/<int:id>/', views.update_item, name="update_item"),

    
    # Function based delete_item view.
    # --------------------------------------------------------------------------------
    path('delete/<int:id>/', views.delete_item, name="delete_item"),

    
    # Function based category view.
    # --------------------------------------------------------------------------------
    # path('category/', views.Category, name='category'),

    path('search/', views.search, name='search'),
    
]



