from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'listapi',views.ListViewset, basename ='lists')
router.register(r'listitem',views.ListItemViewSet,basename = "listitem")

urlpatterns = [
    path('',include(router.urls)),

]