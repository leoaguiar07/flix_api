from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),

    # OPENAPI 3
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path("api/v1/", include('authentication.urls')),
    path("api/v1/", include('genres.urls')),
    path("api/v1/", include('actors.urls')),
    path("api/v1/", include('movies.urls')),
    path("api/v1/", include('reviews.urls')),

]
#TODO: Usar tags para OPENAPI
#TODO: Implementar LOGs.
#TODO: Implementar TESTES: unitário, carga (locust).
#TODO: DOCKERIZAR a aplicação.