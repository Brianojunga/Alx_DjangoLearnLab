from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewset, RegisterViewset, Login, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'users', CustomUserViewset, basename='users')
router.register(r'register', RegisterViewset, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', Login.as_view(), name='login'),
    # "unfollow/<int:user_id>/,
    #follow/<int:user_id>
    #path('profile/', ProfileView.as_view(), name='profile'),
    #path('register/', RegisterView.as_view(), name='register'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post')
]
