from django.urls import path

from . import views

urlpatterns = [
    #/climbs/
    path('', views.index, name='index'),
    #/climbs/places/
    path('locations/',views.locations),
    path('locations/<location_id>/', views.locations),
    path('locations/<location_id>/children', views.getAreasForLocation),

    #/climbs/areas/
    path('areas/',views.areas),
    path('locations/<location_id>/<area_id>/', views.areas), #getPage
    path('locations/<location_id>/<area_id>/children', views.getBouldersForArea), #getChildren

    #/climbs/boulders/
    path('boulders/',views.boulders),
    path('locations/<location_id>/<area_id>/<boulder_id>/', views.boulders), #getPage
    path('locations/<location_id>/<area_id>/<boulder_id>/children', views.getClimbsForBoulder), #getChildren

    #/climbs/climbs/
    path('climbs/',views.climbs),
    path('locations/<location_id>/<area_id>/<boulder_id>/<climb_id>/', views.climbs),
]
