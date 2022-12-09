from django.urls import path
from .views import Index, Detail, Create, Update, Delete

app_name = 'report'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('detail/<int:pk>/', Detail.as_view(), name='detail'),
    path('create/', Create.as_view(), name='create'),
    path('update/<int:pk>', Update.as_view(), name='update'),
    path('delete/<int:pk>', Delete.as_view(), name='delete'),
]