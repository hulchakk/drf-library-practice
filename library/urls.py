from django.contrib import admin
from django.urls import include, path


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
    )
]
