from django.shortcuts import render
from productapp.models import *
from productapp.forms.master_form import *
from django.views.generic import CreateView, View
from productapp.helper import renderfile, is_ajax
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import *
from productapp.constantvariables import PAGINATION_PERPAGE
from django.shortcuts import get_object_or_404
from django.db import transaction
import pdb


class SubCategoryView(View):
    def get(self, request, *args, **kwargs):
        context, response = {}, {}
        page = int(request.GET.get('page', 1))
        subcategories = SubCategory.objects.filter().order_by('-id')
        paginator = Paginator(subcategories, PAGINATION_PERPAGE)
        try:
            subcategories = paginator.page(page)
        except PageNotAnInteger:
            subcategories = paginator.page(1)
        except EmptyPage:
            subcategories = paginator.page(paginator.num_pages)

        context['subcategories'], context['current_page'] = subcategories, page
        if is_ajax(request=request):
            response['status'] = True
            response['pagination'] = render_to_string("subcategory/pagination.html",context=context,request=request)
            response['template'] = render_to_string('subcategory/subcategory_list.html', context, request=request)
            return JsonResponse(response)
        context['form']  = CategoryForm()
        return render(request,'subcategory/index.html',context)      


class SubCategoryCreate(View):
    def get(self, request, *args, **kwargs):
        # print('......')
        data = {}
        form = SubCategoryForm()
        # print(form)
        context = {'form': form, 'id': 0}
        data['status'] = True
        data['title'] = 'Add Subcategory'
        data['template'] = render_to_string('subcategory/subcategory_form.html', context, request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        response = {}
        form = SubCategoryForm(request.POST or None)
        # print(form)
        if form.is_valid():
            # print('mmm')
            try:
                with transaction.atomic():
                    name = request.POST.get('name', None)
                    category = request.POST.get('category', None)

                    # CHECK THE DATA EXISTS
                    if not SubCategory.objects.filter(name=name,category_id=category).exists():
                        obj = SubCategory.objects.create(name=name,category_id=category)

                        response['status'] = True
                        response['message'] = 'Added successfully'
                    else:
                        response['status'] = False
                        response['message'] = 'SubCategory Already exists'

            except Exception as error:
                response['status'] = False
                response['message'] = 'Something went wrong'
        else:
            response['status'] = False
            context = {'form': form}
            response['title'] = 'Edit SubCategory'
            response['valid_form'] = False
            response['template'] = render_to_string('/subcategory/subcategory_form.html', context, request=request)
        return JsonResponse(response)
    

class SubCategoryDelete(View):

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk', None)
        response = {}
        obj = get_object_or_404(SubCategory, id = id)
        # obj.is_active = False
        # obj.save()
        obj.delete()

        response['status'] = True
        response['message'] = "Subcategory deleted successfully"
        return JsonResponse(response)



class SubCategoryUpdate(View):
    # print('kkk')
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk', None)
        print(id)
        data = {}
        obj = get_object_or_404(SubCategory, id = id)
        form = SubCategoryForm(instance=obj)
        print('ll')
        print(form)
        context = {'form': form, 'id': id}
        data['status'] = True
        data['title'] = 'Edit Subcategory'
        data['template'] = render_to_string('subcategory/subcategory_form.html', context, request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        # print('kk')
        data, response = {} , {}
        id = kwargs.get('pk', None)
        obj = get_object_or_404(SubCategory, id=id)
        previous_name = obj.name
        form = SubCategoryForm(request.POST or None, instance=obj)

        if form.is_valid():
            try:
                with transaction.atomic():
                    if SubCategory.objects.filter(name__icontains=request.POST.get('name')).exclude(id=id).exists():
                        response['status'] = False
                        response['message'] = "Name already exists"
                        return JsonResponse(response)
                    obj.name = request.POST.get('name' or None)
                    obj.save()

                    response['status'] = True
                    response['message'] = "Subcategory updated successfully"
                    return JsonResponse(response)
                
            except Exception as dberror:

                response['message'] = "Something went wrong"
                response['status'] = True
        else:
            response['status'] = False
            context = {'form': form}
            response['title'] = 'Edit Subcategory'
            response['valid_form'] = False
            response['template'] = render_to_string('subcategory/subcategory_form.html', context, request=request)
            return JsonResponse(response)