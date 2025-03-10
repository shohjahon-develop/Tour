from django.urls import path

from blog.views import *

urlpatterns = [
    path('',index,name="index"),
    # path('foods/<slug:slug>',fooddetailview,name='foodDetail')
    path("foods/",foods,name="foods"),
    path("medical/",medical,name="medical"),
    path("services/",services,name="services"),
    path('job/',jobs,name="jobs"),
    path("shop/",shopping,name="shop"),
    path("hotels/",hotel,name="hotel"),
    path("auto/",auto,name="auto"),

    path('tips/<int:pk>/', tips_detail, name='tips_detail'),
    path('add-comment/<int:tips_id>/', add_comment, name='add_comment'),
    path('search/',search_view, name='search'),
    # <-- detail pages -->
    path('dir/<int:pk>',dir_detail,name='dir_detail'),
    path('add-comment_2/<int:dir_id>/', add_comment_2, name='add_comment_2')


]