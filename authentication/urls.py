from django.urls import path
from . import views
app_name='user'
urlpatterns=[
    path('all_users/',views.all_users,name='all_users'),
    path('add_user/',views.add_user,name='add_user'),
    path('add_user/<int:id>',views.add_user,name='update_user'),
    path('<int:pk>/',views.UserIdView.as_view(),name='rest_user_by_id'),
    path('list/',views.UserListView.as_view(),name='rest_user_list'),
    path('create/',views.CreateUserView.as_view(),name='rest_user_create'),
    path('<int:id>/order/<int:pk>/',views.OrderByUserView.as_view(),name='rest_order_by_user'),
]