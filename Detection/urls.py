from django.urls import path
from .import views
app_name='Detection'
urlpatterns=[
    path('',views.index,name='index'),
    # path('select/',views.add_pic,name='select'),
    path('detection/', views.upload_image, name='detection')
]