from django.http.response import HttpResponse
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register('Products', views.HomeAPIView)
router.register('Comments', views.CommentAPIView)
router.register('Members', views.UserAPIView)
router.register('Types of products', views.ProductTypeAPIView)

urlpatterns = [
    path('openapi', get_schema_view(
        title="-=Shop for artists=-",
        description="Best API ever",
        version="0.0.1"
    ), name='openapi-schema'),
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('', include(router.urls)),
]

# router.register('Ratings', views.RatingsAPIView)
# router.register('Transactions', views.TransactionsAPIView)
# router.register('Carts', views.CartsAPIView)

# urlpatterns = router.urls
