from django.contrib import admin
from django.urls import path
from .views import TaskViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task_api/',TaskViewSet.as_view({'get':'get', 'post':'post', 'put':'put', 'delete':'delete'})),
    

]
