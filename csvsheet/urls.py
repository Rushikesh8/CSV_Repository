from django.urls import path
from csvsheet.views import upload_file

urlpatterns = [
    path('',upload_file)
]