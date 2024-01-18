from django import forms
from productapp.models import *


class CountryForm(forms.ModelForm):
    name = forms.CharField( 
        label="Title", max_length=200, required = True,
        widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control'}),
        error_messages={ 'required': 'The name should not be empty' }
    )
    
    class Meta:
        model = Country
        fields = ['name']


class RegionForm(forms.ModelForm):
    name = forms.CharField( 
        label="Title", max_length=200, required = True,
        widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control'}),
        error_messages={ 'required': 'The region name should not be empty' }
    )

    country = forms.ModelChoiceField(
                    required=True, 
                    empty_label='Select a country',
                    queryset=Country.objects.all(),
                    widget=forms.Select(attrs={'class':'form-control'}),
                    error_messages={ 'required': 'The country name should not be empty' })
    
    class Meta:
        model = Region
        fields = ['name','country']


class BrandForm(forms.ModelForm):
    name = forms.CharField( 
        label="Title", max_length=200, required = True,
        widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control'}),
        error_messages={ 'required': 'The brand name should not be empty' }
    )

    division = forms.ModelChoiceField(
                    required=True, 
                    empty_label='Select a division',
                    queryset=Division.objects.all(),
                    widget=forms.Select(attrs={'class':'form-control'}),
                    error_messages={ 'required': 'The division name should not be empty' })

    
    class Meta:
        model = Brand
        fields = ['name','division']



class DivisionForm(forms.ModelForm):
    name = forms.CharField( 
        label="Title", max_length=200, required = True,
        widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control'}),
        error_messages={ 'required': 'The name should not be empty' }
    )

    sku_classification = forms.ModelChoiceField(
                    required=True, 
                    empty_label='Select SKU Classification',
                    queryset=Sku_Classification.objects.all(),
                    widget=forms.Select(attrs={'class':'form-control'}),
                    error_messages={ 'required': 'The SKU Classification should not be empty' })
    
    screen = forms.BooleanField(
                    label="Screen",required=False,
                    widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    class Meta:
        model = Division
        fields = ['name','screen','sku_classification']


   

class CategoryForm(forms.ModelForm):
    name = forms.CharField( 
        label="Title", max_length=200, required = True,
        widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control'}),
        error_messages={ 'required': 'The name should not be empty' }
    )

    division = forms.ModelChoiceField(
                    required=True, 
                    empty_label='Select a division',
                    queryset=Division.objects.all(),
                    widget=forms.Select(attrs={'class':'form-control'}),
                    error_messages={ 'required': 'The division name should not be empty' })
    
    class Meta:
        model = Category
        fields = ['name','division']


class SubCategoryForm(forms.ModelForm):
    name = forms.CharField( 
        label="Title", max_length=200, required = True,
        widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control'}),
        error_messages={ 'required': 'The name should not be empty' }
    )
    
    category = forms.ModelChoiceField(
                    required=True, 
                    empty_label='Select a Category',
                    queryset=Category.objects.all().distinct(),
                    widget=forms.Select(attrs={'class':'form-control'}),
                    error_messages={ 'required': 'The category should not be empty'})
    
    class Meta:
        model = SubCategory
        fields = ['name','category']


class SkuClassificationForm(forms.ModelForm):
    name = forms.CharField( 
        label="Title", max_length=200, required = True,
        widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control'}),
        error_messages={ 'required': 'The name should not be empty' }
    )


    class Meta:
        model = Sku_Classification
        fields = ['name']


class ScreenSizeForm(forms.ModelForm):
    screensize = forms.CharField( 
        label="ScreenSize",required = True,
        widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Enter screensize'}),
        error_messages={ 'required': 'The screensize should not be empty' }
    )
    class Meta:
        model = ScreenSize
        fields = ['screensize']


