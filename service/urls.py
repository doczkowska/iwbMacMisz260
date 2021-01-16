from django.urls import path
from service.views import list_, preview, create, update, delete

urlpatterns = [
    path("", list_, name="service-list"),
    path("preview/<int:pk>/", preview, name="service-preview"),
    path("create/", create, name="service-create"),
    path("update/<int:pk>/", update, name="service-update"),
    path("delete/<int:pk>/", delete, name="service-delete")
    
]