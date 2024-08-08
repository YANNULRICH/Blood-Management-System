from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter, SimpleRouter

from blood.mblood.api.viewsets import *
from blood.users.api.viewsets import TokenObtainPairView, TokenRefreshView
from django.conf import settings

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("donor", DonorViewSet)
router.register("blood_bank", BloodBankViewSet)
router.register("blood_donation", BloodDonationViewSet)
router.register("blood_type", BloodTypeViewSet)
router.register("blood_bag", BloodBagViewSet)
router.register("hospital", HospitalViewSet)
router.register("users", UsersViewSet)
router.register("Command", CommandViewSet)


app_name = "v1"
urlpatterns = router.urls

urlpatterns += [
    # DRF auth token
    path('auth/token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('auth/refresh-token/', TokenRefreshView.as_view(), name='token-refresh'),

    # path("auth/token/", TokenObtainPairView.as_view(), name="auth_token"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="v1:schema"),
        name="docs",
    ),

]


