from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'images', views.ImagesViewSet)
router.register(r'album', views.AlbumViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('add_image', views.AddImageAPI.as_view()),
    path('add_album', views.AddAlbumAPI.as_view()),
    path('edit_album/<int:pk>', views.editAlbumAPI.as_view()),

]