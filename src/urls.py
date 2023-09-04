from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# from announcement.api import MentorView, AnnouncementCreateView, AnnouncementRetrieveUpdateDestroyView
# AnnouncementRetrieveView, AnnouncementUpdateView, AnnouncementDeleteView,
urlpatterns = [
    path('admin/', admin.site.urls),
    path('announcement/', include('announcement.urls')),
    # path("announcement/<int:pk>/",AnnouncementRetrieveUpdateDestroyView.as_view()),
    # path('announcement-update/<int:pk>/', AnnouncementUpdateView.as_view()),
    # path('announcement-delete/<int:pk>/', AnnouncementDeleteView.as_view()),
    # path('announcement-create/', AnnouncementCreateView.as_view())
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


