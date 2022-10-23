from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.allBlogs , name=""),
    path('create_blog/', views.createBlog, name="create-blog"),
    path('edit_blog/<str:pk>', views.editBlog, name="edit-blog"),
    path('delete_blog/<str:pk>', views.deleteBlog, name="delete-blog"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
