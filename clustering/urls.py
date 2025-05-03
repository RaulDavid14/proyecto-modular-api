from django.urls import path
from .views import ClusteringView, clustering_template, ClusteringAPIView


urlpatterns = [
    path("json/", ClusteringView.as_view(), name="clustering_json"),
    path("template/", clustering_template, name="clustering_template"),
    path("", ClusteringAPIView.as_view(), name="api_clustering"), 
]

