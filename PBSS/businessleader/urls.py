from django.urls import path
from .views import PostListViewBl, PostListViewBlSw, PostDetailViewBl, PostDeleteViewBl
from . import views
from businessleader import views as LeaderView

urlpatterns = [
    path('', PostListViewBl.as_view(), name='BL_view'),
    path('registerSW/', LeaderView.blregister, name='businessleader'),
    path('supportworker/',PostListViewBlSw, name='supportworker'),
    path('user/<int:user_id>/delete',PostDeleteViewBl, name='user_delete'),
    path('user/<int:pk>/', PostDetailViewBl.as_view(), name='user-detail'),

]