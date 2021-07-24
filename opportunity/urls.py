from django.urls import path
from . import views

app_name = "opportunity"

urlpatterns = [
    path("create/",views.OpportunityCreateView.as_view(), name="create"),
    path("",views.OpportunityListView.as_view(), name="list"),
]
