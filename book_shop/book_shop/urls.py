
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reader.urls')),
    path('books/',include('books.urls'))
]
