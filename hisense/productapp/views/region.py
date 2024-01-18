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



class RegionView(View):
    def get(self, request, *args, **kwargs):
        context, response = {}, {}
        page = int(request.GET.get('page', 1))
        regions = Region.objects.filter().order_by('-id')
        paginator = Paginator(regions, PAGINATION_PERPAGE)
        try:
            regions = paginator.page(page)
        except PageNotAnInteger:
            regions = paginator.page(1)
        except EmptyPage:
            regions = paginator.page(paginator.num_pages)

        context['regions'], context['current_page'] = regions, page
        if is_ajax(request=request):
            response['status'] = True
            response['pagination'] = render_to_string("region/pagination.html",context=context,request=request)
            response['template'] = render_to_string('region/region_list.html', context, request=request)
            return JsonResponse(response)
        context['form']  = RegionForm()
        return render(request,'region/index.html',context)  
    


class RegionCreate(View):
    def get(self, request, *args, **kwargs):
        print('......')
        data = {}
        form = RegionForm()
        # print(form)
        context = {'form': form, 'id': 0}
        data['status'] = True
        data['title'] = 'Add Region'
        data['template'] = render_to_string('region/region_form.html', context, request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        response = {}
        form = RegionForm(request.POST or None)
        # print(form)
        if form.is_valid():
            # print('mmm')
            try:
                with transaction.atomic():
                    region = request.POST.get('name', None)
                    country = request.POST.get('country', None)

                    # CHECK THE DATA EXISTS
                    if not Region.objects.filter(name=region,country_id=country).exists():
                        obj = Region.objects.create(name=region,country_id=country)

                        response['status'] = True
                        response['message'] = 'Added successfully'
                    else:
                        response['status'] = False
                        response['message'] = 'Region Already exists'

            except Exception as error:
                response['status'] = False
                response['message'] = 'Something went wrong'
        else:
            response['status'] = False
            context = {'form': form}
            response['title'] = 'Edit Region'
            response['valid_form'] = False
            response['template'] = render_to_string('region/region_form.html', context, request=request)
        return JsonResponse(response)



class RegionDelete(View):

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk', None)
        response = {}
        obj = get_object_or_404(Region, id = id)
        # obj.is_active = False
        # obj.save()
        obj.delete()

        response['status'] = True
        response['message'] = "Region deleted successfully"
        return JsonResponse(response)
    


class RegionUpdate(View):
    # print('kkk')
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk', None)
        print(id)
        data = {}
        obj = get_object_or_404(Region, id = id)
        form = RegionForm(instance=obj)
        print('ll')
        print(form)
        context = {'form': form, 'id': id}
        data['status'] = True
        data['title'] = 'Edit Region'
        data['template'] = render_to_string('region/region_form.html', context, request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        # print('kk')
        data, response = {} , {}
        id = kwargs.get('pk', None)
        obj = get_object_or_404(Region, id=id)
        form = RegionForm(request.POST or None, instance=obj)

        if form.is_valid():
            region = request.POST.get('name', None)
            country = request.POST.get('country', None)
            try:
                with transaction.atomic():
                    if Region.objects.filter(name__icontains=region,country_id=country).exclude(id=id).exists():
                        response['status'] = False
                        response['message'] = "Name already exists"
                        return JsonResponse(response)
                    obj.name = request.POST.get('name' or None)
                    obj.save()

                    response['status'] = True
                    response['message'] = "Region updated successfully"
                    return JsonResponse(response)
                
            except Exception as dberror:
                response['message'] = "Something went wrong"
                response['status'] = True
        else:
            response['status'] = False
            context = {'form': form}
            response['title'] = 'Edit Region'
            response['valid_form'] = False
            response['template'] = render_to_string('region/region_form.html', context, request=request)
            return JsonResponse(response)