from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewset, RegisterViewset, LoginViewset

router = DefaultRouter()
router.register(r'users', CustomUserViewset, basename='users')
router.register(r'register', RegisterViewset, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginViewset.as_view(), name='login'),
    #path('profile/', ProfileView.as_view(), name='profile'),
    #path('register/', RegisterView.as_view(), name='register'),
]
