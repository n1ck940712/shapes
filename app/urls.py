from rest_framework.documentation import include_docs_urls
from django.urls import path
from . import views

urlpatterns = [
    path('docs/', include_docs_urls(title='Shapes Api')),

    path("",views.ListShapeAPIView.as_view(),name="shape_list"),
    path("<int:pk>/",views.ListShapeDetailsAPIView.as_view(),name="shape_list"),
    path("create/", views.CreateShapeAPIView.as_view(),name="shape_create"),
    path("update/<int:pk>/",views.UpdateShapeAPIView.as_view(),name="shape_update"),
    path("delete/<int:pk>/",views.DeleteShapeAPIView.as_view(),name="shape_delete")
]
