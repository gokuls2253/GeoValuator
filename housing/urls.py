from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.project, name='project'),
    path('environment', views.environment, name='environment'),
    path('culture/', views.culture, name='culture'),
    path('api/predict/', views.predict_price, name='predict_price_api'),
]

