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




class CountryView(View):
    def get(self, request, *args, **kwargs):
        context, response = {}, {}
        page = int(request.GET.get('page', 1))
        countries = Country.objects.filter(is_active=True).order_by('-id')
        paginator = Paginator(countries, PAGINATION_PERPAGE)
        try:
            countries = paginator.page(page)
        except PageNotAnInteger:
            countries = paginator.page(1)
        except EmptyPage:
            countries = paginator.page(paginator.num_pages)

        context['countries'], context['current_page'] = countries, page
        if is_ajax(request=request):
            response['status'] = True
            response['pagination'] = render_to_string("country/pagination.html",context=context,request=request)
            response['template'] = render_to_string('country/country_list.html', context, request=request)
            return JsonResponse(response)
        context['form']  = CountryForm()
        # return renderfile(request, 'country', 'index', context)
        return render(request,'country/index.html',context)
    
class CountryCreate(View):
    def get(self, request, *args, **kwargs):
        # print('......')
        data = {}
        form = CountryForm()
        # print(form)
        context = {'form': form, 'id': 0}
        data['status'] = True
        data['title'] = 'Add Country'
        data['template'] = render_to_string('country/country_form.html', context, request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        response = {}
        form = CountryForm(request.POST or None)
        # print(form)
        if form.is_valid():
            # print('mmm')
            try:
                with transaction.atomic():
                    name = request.POST.get('name', None)
                    # CHECK THE DATA EXISTS
                    if not Country.objects.filter(name=name).exists():
                        obj = Country.objects.create(name=name)
                     
                        response['status'] = True
                        response['message'] = 'Added successfully'
                    else:
                        response['status'] = False
                        response['message'] = 'Country Already exists'

            except Exception as error:
                response['status'] = False
                response['message'] = 'Something went wrong'
        else:
            response['status'] = False
            context = {'form': form}
            response['title'] = 'Edit Country'
            response['valid_form'] = False
            response['template'] = render_to_string('/country/country_form.html', context, request=request)
        return JsonResponse(response)
    

class CountryDelete(View):

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk', None)
        response = {}
        obj = get_object_or_404(Country, id = id)
        obj.delete()
        response['status'] = True
        response['message'] = "Country deleted successfully"
        return JsonResponse(response)
    

class CountryUpdate(View):
    # print('kkk')
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk', None)
        print(id)
        data = {}
        obj = get_object_or_404(Country, id = id)
        form = CountryForm(instance=obj)
        print(form)
        context = {'form': form, 'id': id}
        data['status'] = True
        data['title'] = 'Edit Country'
        data['template'] = render_to_string('country/country_form.html', context, request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        # print('kk')
        data, response = {} , {}
        id = kwargs.get('pk', None)
        obj = get_object_or_404(Country, id=id)
        previous_name = obj.name
        form = CountryForm(request.POST or None, instance=obj)

        if form.is_valid():
            try:
                with transaction.atomic():
                    if Country.objects.filter(name__icontains=request.POST.get('name')).exclude(id=id).exists():
                        response['status'] = False
                        response['message'] = "Name already exists"
                        return JsonResponse(response)
                    obj.name = request.POST.get('name' or None)

                    obj.save()

                    response['status'] = True
                    response['message'] = "Country updated successfully"
                    return JsonResponse(response)
                
            except Exception as dberror:

                response['message'] = "Something went wrong"
                response['status'] = True
        else:
            response['status'] = False
            context = {'form': form}
            response['title'] = 'Edit Country'
            response['valid_form'] = False
            response['template'] = render_to_string('country/country_form.html', context, request=request)
            return JsonResponse(response)