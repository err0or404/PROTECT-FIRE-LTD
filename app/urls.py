from django.urls import path
from app.views import index,EngineerSide,LoadEngineerDataInPdf,UpdateFormView,DetailFormView,EngineersReportsList

app_name= "app"
urlpatterns = [
    path('',EngineerSide.as_view(),name="home"),
    path('return/',index,name="return"),
    path('update/<id>/',UpdateFormView.as_view(), name="update"),
    path('detail/<id>/',DetailFormView.as_view(), name="detail"),

    path('<int:id>/',LoadEngineerDataInPdf, name = "loadDrawing"),

    path('pendinglist/',EngineersReportsList.as_view(),name="pendinglist")

]