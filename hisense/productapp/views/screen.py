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


class ScreenSizeView(View):
    def get(self, request, *args, **kwargs):
        context, response = {}, {}
        page = int(request.GET.get('page', 1))
        screensizes = ScreenSize.objects.filter().order_by('-id')
        paginator = Paginator(screensizes, PAGINATION_PERPAGE)
        try:
            screensizes = paginator.page(page)
        except PageNotAnInteger:
            screensizes = paginator.page(1)
        except EmptyPage:
            screensizes = paginator.page(paginator.num_pages)

        context['screensizes'], context['current_page'] = screensizes, page
        if is_ajax(request=request):
            response['status'] = True
            response['pagination'] = render_to_string("screensize/pagination.html",context=context,request=request)
            response['template'] = render_to_string('screensize/screensize.html', context, request=request)
            return JsonResponse(response)
        context['form']  = ScreenSizeForm()
        return render(request,'screensize/index.html',context)      



class ScreenSizeCreate(View):
    def get(self, request, *args, **kwargs):
        # print('......')
        data = {}
        form = ScreenSizeForm()
        # print(form)
        context = {'form': form, 'id': 0}
        data['status'] = True
        data['title'] = 'Add Screensize'
        data['template'] = render_to_string('screensize/screensize_form.html', context, request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        response = {}
        form = ScreenSizeForm(request.POST or None)
        # print(form)
        if form.is_valid():
            # print('mmm')
            try:
                with transaction.atomic():
                    screensize = request.POST.get('screensize', None)
                    # CHECK THE DATA EXISTS
                    if not ScreenSize.objects.filter(screensize=screensize).exists():
                        obj = ScreenSize.objects.create(screensize=screensize)

                        response['status'] = True
                        response['message'] = 'Added successfully'
                    else:
                        response['status'] = False
                        response['message'] = 'Screensize Already exists'

            except Exception as error:
                response['status'] = False
                response['message'] = 'Something went wrong'
        else:
            response['status'] = False
            context = {'form': form}
            response['title'] = 'Add Screensize'
            response['valid_form'] = False
            response['template'] = render_to_string('/screensize/screensize_form.html', context, request=request)
        return JsonResponse(response)


class ScreenSizeUpdate(View):
    # print('kkk')
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk', None)
        print(id)
        data = {}
        obj = get_object_or_404(ScreenSize, id = id)
        form = ScreenSizeForm(instance=obj)
        # print('ll')
        # print(form)
        context = {'form': form, 'id': id}
        data['status'] = True
        data['title'] = 'Edit Screensize'
        data['template'] = render_to_string('screensize/screensize_form.html', context, request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        print('kk')
        response = {}
        id = kwargs.get('pk', None)
        obj = get_object_or_404(ScreenSize, id=id)
        # previous_name = obj.screensize
        form = ScreenSizeForm(request.POST or None, instance=obj)
        # print(form)

        if form.is_valid():
            # print('ljbj')
            try:
                with transaction.atomic():
                    if ScreenSize.objects.filter(screensize__icontains=request.POST.get('screensize')).exclude(id=id).exists():
                        print(',,,,,')
                        
                        response['status'] = False
                        response['message'] = "Screensize already exists"
                        return JsonResponse(response)
                    else:
                        print(',,,,,')
                        obj.screensize = request.POST.get('screensize' or None)
                        obj.save()

                        response['status'] = True
                        response['message'] = "Screensize updated successfully"
                    return JsonResponse(response)
                
            except Exception as dberror:

                response['message'] = "Something went wrong"
                response['status'] = True
                return JsonResponse(response)

        else:
            response['status'] = False
            context = {'form': form}
            response['title'] = 'Edit Screensize'
            response['valid_form'] = False
            response['template'] = render_to_string('screensize/screensize_form.html', context, request=request)
            return JsonResponse(response)
        


class ScreenSizeDelete(View):
    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk', None)
        response = {}
        obj = get_object_or_404(ScreenSize, id = id)
        # obj.is_active = False
        # obj.save()
        obj.delete()

        response['status'] = True
        response['message'] = "Screensize deleted successfully"
        return JsonResponse(response)