"""ITIS_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.histories import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('imb/', views.calc_imb, name='calc_imb'),
    path('filter_imb/', views.filter_data, name='filter_imb'),
    # path('v/update/<int:history_id>', views.imb_update, name='imb_update'),
    path('imb/update/<int:pk>', views.IMBUpdate.as_view(), name='imb_update'),
    path('imb/delete/<int:pk>', views.IMBDelete.as_view(), name='imb_delete'),

    # path('filter_weight/', views.filter_weight, name='filter_weight'),
]
