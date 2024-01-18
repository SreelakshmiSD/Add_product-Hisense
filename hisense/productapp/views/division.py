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


class DivisionView(View):
    def get(self, request, *args, **kwargs):
        context, response = {}, {}
        page = int(request.GET.get('page', 1))
        divisions = Division.objects.filter().order_by('-id')
        paginator = Paginator(divisions, PAGINATION_PERPAGE)
        try:
            divisions = paginator.page(page)
        except PageNotAnInteger:
            divisions = paginator.page(1)
        except EmptyPage:
            divisions = paginator.page(paginator.num_pages)

        context['divisions'], context['current_page'] = divisions, page
        if is_ajax(request=request):
            response['status'] = True
            response['pagination'] = render_to_string("division/pagination.html",context=context,request=request)
            response['template'] = render_to_string('division/brand_list.html', context, request=request)
            return JsonResponse(response)
        context['form']  = BrandForm()
        return render(request,'division/index.html',context)


class DivisionCreate(View):
    def get(self, request, *args, **kwargs):
        print('......')
        data = {}
        form = DivisionForm()
        print(form)
        context = {'form': form, 'id': 0}
        data['status'] = True
        data['title'] = 'Add Division'
        data['template'] = render_to_string('division/division_form.html', context, request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        response = {}
        form = DivisionForm(request.POST or None)
        # print(form)
        if form.is_valid():
            try:
                with transaction.atomic():
                    name = request.POST.get('name', None)
                    sku_classification = request.POST.get('sku_classification',None)
                    screen = request.POST.get('screen')
                    if screen==None:
                        screen=False
                    else:
                        screen=True

                    name=name.upper()
                    # CHECK THE DATA EXISTS
                    if not Division.objects.filter(name=name,sku_classification_id=sku_classification).exists():
                        obj = Division.objects.create(name=name,sku_classification_id=sku_classification,screen=screen)
                        obj.save()
                        # print(obj)
                        response['status'] = True
                        response['message'] = 'Added successfully'
                    else:
                        response['status'] = False
                        response['message'] = 'Division Already exists'

            except Exception as error:
                response['status'] = False
                response['message'] = 'Something went wrong'
        else:
            response['status'] = False
            context = {'form': form}
            response['title'] = 'Add Division'
            response['valid_form'] = False
            response['template'] = render_to_string('division/division_form.html', context, request=request)
        return JsonResponse(response)


class DivisionDelete(View):
    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk', None)
        response = {}
        obj = get_object_or_404(Division, id = id)
       
        obj.delete()
       

        response['status'] = True
        response['message'] = "Division deleted successfully"
        return JsonResponse(response)   

class DivisionUpdate(View):
    # print('kkk')
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk', None)
        print(id)
        data = {}
        obj = get_object_or_404(Division, id = id)
        print(obj.screen)

        form = DivisionForm(instance=obj)
        print('ll')

        # print(form)
        context = {'form': form, 'id': id}
        data['status'] = True
        data['title'] = 'Edit Division'
        data['template'] = render_to_string('division/division_form.html', context, request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        print('kk')
        data, response = {} , {}
        id = kwargs.get('pk', None)
        obj = get_object_or_404(Division, id=id)
        previous_name = obj.name
        form = DivisionForm(request.POST or None, instance=obj)
        # print(form)
        if form.is_valid():
            print('lljh')
            division = request.POST.get('name')
            sku_classification = request.POST.get('sku_classification')
            screen = request.POST.get('screen')
            if screen==None:
                screen=False
            else:
                screen=True
            try:
                with transaction.atomic():
                    if Division.objects.filter(name__icontains=division,sku_classification_id=sku_classification).exclude(id=id).exists():
                        response['status'] = False
                        response['message'] = "Division already exists"
                        return JsonResponse(response)
                    else:
                        obj.name = division
                        obj.screen = screen
                        obj.sku_classification_id= sku_classification
                        obj.save()
                        response['status'] = True
                        response['message'] = "Division updated successfully"
                        return JsonResponse(response)
                
            except Exception as dberror:
                response['message'] = "Something went wrong"
                response['status'] = True
                return JsonResponse(response)

        else:
            response['status'] = False
            context = {'form': form}
            response['title'] = 'Edit Division'
            response['valid_form'] = False
            response['template'] = render_to_string('division/division_form.html', context, request=request)
            return JsonResponse(response)