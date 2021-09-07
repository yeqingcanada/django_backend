from django.conf.urls import url
from django.urls import path
from Product import views
from Product import UploadFileView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    # url(r'^department$',views.departmentApi),
    # url(r'^bulkcreate$', UploadFileView.UploadFile),
    # url(r'^hello$', views.my_view)
    path('hello', views.my_view),
    path('department', views.departmentApi),
    path('bulkcreate', UploadFileView.UploadFile)

]