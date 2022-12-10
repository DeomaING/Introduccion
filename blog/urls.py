from django.urls import path
from .views import BlogListView, BlogCreateView,BlogDetailView, Update_view,BlogDeleteView

app_name="blog"

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", Update_view.as_view(), name="update"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="delete")
]