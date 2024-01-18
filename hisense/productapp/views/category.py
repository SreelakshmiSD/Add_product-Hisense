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

class CategoryView(View):
    def get(self, request, *args, **kwargs):
        context, response = {}, {}
        page = int(request.GET.get('page', 1))
        categories = Category.objects.filter().order_by('-id')
        paginator = Paginator(categories, PAGINATION_PERPAGE)
        try:
            categories = paginator.page(page)
        except PageNotAnInteger:
            categories = paginator.page(1)
        except EmptyPage:
            categories = paginator.page(paginator.num_pages)

        context['categories'], context['current_page'] = categories, page
        if is_ajax(request=request):
            response['status'] = True
            response['pagination'] = render_to_string("category/pagination.html",context=context,request=request)
            response['template'] = render_to_string('category/category_list.html', context, request=request)
            return JsonResponse(response)
        context['form']  = CategoryForm()
        return render(request,'category/index.html',context)      


class CategoryCreate(View):
    def get(self, request, *args, **kwargs):
        print('......')
        data = {}
        form = CategoryForm()
        context = {'form': form, 'id': 0}
        data['status'] = True
        data['title'] = 'Add Category'
        data['template'] = render_to_string('category/category_form.html', context, request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        response = {}
        form = CategoryForm(request.POST or None)
        division = request.POST.get('division', None)
        # print(division)
        # print(form)
        if form.is_valid():
            # print('mmm')
            try:
                with transaction.atomic():
                    name = request.POST.get('name', None)
                    division = request.POST.get('division', None)

                    # CHECK THE DATA EXISTS
                    if not Category.objects.filter(name=name,division_id=division).exists():
                        obj = Category.objects.create(name=name,division_id=division)

                        response['status'] = True
                        response['message'] = 'Added successfully'
                    else:
                        response['status'] = False
                        response['message'] = 'Category Already exists'

            except Exception as error:
                response['status'] = False
                response['message'] = 'Something went wrong'
        else:
            response['status'] = False
            context = {'form': form}
            response['title'] = 'Add Category'
            response['valid_form'] = False
            response['template'] = render_to_string('category/category_form.html', context, request=request)
        return JsonResponse(response)



class CategoryDelete(View):
    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk', None)
        response = {}
        obj = get_object_or_404(Category, id = id)
        # obj.is_active = False
        # obj.save()
        obj.delete()
        response['status'] = True
        response['message'] = "Category deleted successfully"
        return JsonResponse(response)


class CategoryUpdate(View):
    # print('kkk')
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk', None)
        print(id)
        data = {}
        obj = get_object_or_404(Category, id = id)
        form = CategoryForm(instance=obj)
        print('ll')
        print(form)
        context = {'form': form, 'id': id}
        data['status'] = True
        data['title'] = 'Edit Category'
        data['template'] = render_to_string('category/category_form.html', context, request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        # print('kk')
        data, response = {} , {}
        id = kwargs.get('pk', None)
        obj = get_object_or_404(Category, id=id)
        previous_name = obj.name
        form = CategoryForm(request.POST or None, instance=obj)

        if form.is_valid():
            try:
                with transaction.atomic():
                    if Category.objects.filter(name__icontains=request.POST.get('name')).exclude(id=id).exists():
                        response['status'] = False
                        response['message'] = "Name already exists"
                        return JsonResponse(response)
                    else:
                        obj.name = request.POST.get('name' or None)
                        obj.name = request.POST.get('name' or None)
                        obj.save()
                        response['status'] = True
                        response['message'] = "Category updated successfully"
                        return JsonResponse(response)
                
            except Exception as dberror:
                response['message'] = "Something went wrong"
                response['status'] = True
        else:
            response['status'] = False
            context = {'form': form}
            response['title'] = 'Edit Category'
            response['valid_form'] = False
            response['template'] = render_to_string('category/category_form.html', context, request=request)
            return JsonResponse(response)