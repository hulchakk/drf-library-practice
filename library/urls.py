from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/book_service/", include(
        "book_service.urls",
        namespace="book_service"
        )
    ),
    path("api/user/", include(
        "user.urls",
        namespace="user"
        )
    ),
    path("api/borrowing_service/", include(
        "borrowing_service.urls",
        namespace="borrowing_service"
        )
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
