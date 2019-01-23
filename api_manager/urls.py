from rest_framework.routers import SimpleRouter
from .views import UserViewSet, ReservationViewSet, \
    ParkingSlotView
from django.conf.urls import url

router = SimpleRouter()
router.trailing_slash = '/?'
# API for user registration GET, PUT, POST, DELETE
router.register(r'users', UserViewSet)
#  API for POST, GET, UPDATE, DELETE reservations
router.register(r'reservations', ReservationViewSet)


urlpatterns = []
urlpatterns += router.urls
urlpatterns += [url(r'^parking_slots/', ParkingSlotView.as_view(),
                    name="parking_slots")]

