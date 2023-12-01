from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),  
    path('', include('library.urls')), 

    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'), 
]
