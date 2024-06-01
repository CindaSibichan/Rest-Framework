from django.urls import path,include
from restapp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'person_view',PersonViewSet, basename=person_view)
urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('index/',index , name="index" ),
    path('person_view/',person_view,name="person_view"),
    path('ClassPerson/', ClassPerson.as_view() , name="ClassPerson"),
    path('GenericPerson/',GenericPerson.as_view() , name="GenericPerson"),
    path('GenericPerson/<id>/',GenericPersonUpdate.as_view(), name="GenericPersonUpdate"),
]
