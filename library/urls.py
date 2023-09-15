from django.urls import path

from.views import UploadFileView

urlpatterns = [
    path("", UploadFileView, name="upload_book",)
]