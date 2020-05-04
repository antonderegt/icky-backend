"""icky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from problems import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/problems/$', views.problems_list, name="get_post_problems"),
    url(r'^api/problems/(?P<pk>[0-9]+)$', views.problem_detail, name="get_delete_update_problem"),
    url(r'^api/problems/(?P<pk>[0-9]+)/categories$', views.problem_categories, name="get_delete_update_problem_categories"),
    url(r'^api/problems/(?P<problemPk>[0-9]+)/(?P<catPk>[0-9]+)$', views.category_detail),
    url(r'^api/problems/(?P<problemPk>[0-9]+)/(?P<catPk>[0-9]+)/(?P<itemPk>[0-9]+)$', views.item_detail),
]
