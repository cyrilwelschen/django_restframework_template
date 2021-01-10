from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
]


# following should be at end of the file
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]