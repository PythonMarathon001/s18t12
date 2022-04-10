from django.urls import path

from . import views

app_name = 'author'
urlpatterns = [
    # path('', views.index, name='index'),
    path('all_authors', views.all_authors, name='all_authors'),
    path('add_author', views.add_author, name='add_author'),
    path('add_author/<int:id>', views.add_author, name='update_author'),

    path('list/',views.AuthorListView.as_view(),name='rest_all_authors'),
    path('<int:pk>/',views.AuthorByIdView.as_view(),name='rest_author_by_id'),
    path('create/',views.AuthorCreateView.as_view(),name='rest_create_authorr')
]