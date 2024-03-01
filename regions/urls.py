from django.urls import path
from . import views


urlpatterns = [
    path("", views.ViloyatListView.as_view(), name="viloyat-list"),
    path(
        "viloyatlar/<int:pk>/", views.ViloyatDetailView.as_view(), name="viloyat-detail"
    ),
    path(
        "tumanlar/<int:pk>/",
        views.TumanDetailView.as_view(),
        name="tuman-detail",
    ),
    path(
        "mahallalar/<int:pk>/",
        views.MahallaDetailView.as_view(),
        name="mahalla-detail",
    ),
    path(
        "year/<int:pk>/",
        views.YearDetailView.as_view(),
        name="year-detail",
    ),
]
