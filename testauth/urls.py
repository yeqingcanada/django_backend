from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from rest_framework.authtoken.views import obtain_auth_token

from Product import views
from Product import UploadFileView

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^', include('Product.urls')),
    path('auth', obtain_auth_token),
    path('', include('Product.urls'))
]
