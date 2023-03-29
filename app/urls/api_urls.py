from django.urls import path
from app.apis import test_api

urlpatterns = [
    path("user_api", test_api),
]