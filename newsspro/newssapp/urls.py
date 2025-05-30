from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView, CustomTokenObtainPairView, UserDetailView, ChangePasswordView,
    ArticleListView, ArticleDetailView,
    BookmarkListCreateView, BookmarkDeleteView,
    CategoryViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/user/', UserDetailView.as_view(), name='get_user_details'),
    path('auth/change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('bookmarks/', BookmarkListCreateView.as_view(), name='bookmark_list_create'),
    path('bookmarks/<int:bookmark_id>/', BookmarkDeleteView.as_view(), name='bookmark_delete'),
    path('', include(router.urls)),
]
