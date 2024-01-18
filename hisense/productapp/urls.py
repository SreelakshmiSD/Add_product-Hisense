from django.urls import path
from productapp.views.dashboard import *
from productapp.views.country import *
from productapp.views.region import *
from productapp.views.brand import *
from productapp.views.division import *
from productapp.views.category import *
from productapp.views.sub_category import *
from productapp.views.sku_classification import *
from productapp.views.screen import *



app_name = "appproductapp"


urlpatterns = [
    path("", Dashboard.as_view(), name="index"),

    # Country
    path("country/", CountryView.as_view(), name="country"),
    path('country/create/', CountryCreate.as_view(), name='create_country'),
    path('country/<int:pk>/delete/', CountryDelete.as_view(), name='delete_country'),
    path('country/<int:pk>/update/', CountryUpdate.as_view(), name='update_country'),


    # Brand
    path("brand/", BrandView.as_view(), name="brand"),
    path('brand/create/', BrandCreate.as_view(), name='create_brand'),
    path('brand/<int:pk>/delete/', BrandDelete.as_view(), name='delete_brand'),
    path('brand/<int:pk>/update/', BrandUpdate.as_view(), name='update_brand'),


    # Division

    path("division/", DivisionView.as_view(), name="division"),
    path('division/create/', DivisionCreate.as_view(), name='create_division'),
    path('division/<int:pk>/delete/', DivisionDelete.as_view(), name='delete_division'),
    path('division/<int:pk>/update/', DivisionUpdate.as_view(), name='update_division'),


    # Region

    path("region/", RegionView.as_view(), name="region"),
    path('region/create/', RegionCreate.as_view(), name='create_region'),
    path('region/<int:pk>/delete/', RegionDelete.as_view(), name='delete_region'),
    path('region/<int:pk>/update/', RegionUpdate.as_view(), name='update_region'),


    # Category
    path("category/", CategoryView.as_view(), name="category"),
    path('category/create/', CategoryCreate.as_view(), name='create_category'),
    path('category/<int:pk>/delete/', CategoryDelete.as_view(), name='delete_category'),
    path('category/<int:pk>/update/', CategoryUpdate.as_view(), name='update_category'),


    # Sub Category

    path("subcategory/", SubCategoryView.as_view(), name="subcategory"),
    path('subcategory/create/', SubCategoryCreate.as_view(), name='create_subcategory'),
    path('subcategory/<int:pk>/delete/', SubCategoryDelete.as_view(), name='delete_subcategory'),
    path('subcategory/<int:pk>/update/', SubCategoryUpdate.as_view(), name='update_subcategory'),



    # SKU Classification

    path("sku_classification/", SkuClassificationView.as_view(), name="sku_classification"),
    path('sku_classification/create/', SkuClassificationCreate.as_view(), name='create_sku_classification'),
    path('sku_classification/<int:pk>/delete/', SkuClassificationDelete.as_view(), name='delete_sku_classification'),
    path('sku_classification/<int:pk>/update/', SkuClassificationUpdate.as_view(), name='update_sku_classification'),


    # ScreenSize
    path("screensize/", ScreenSizeView.as_view(), name="screensize"),
    path('screensize/create/', ScreenSizeCreate.as_view(), name='create_screensize'),
    path('screensize/<int:pk>/delete/', ScreenSizeDelete.as_view(), name='delete_screensize'),
    path('screensize/<int:pk>/update/', ScreenSizeUpdate.as_view(), name='update_screensize'),


]
