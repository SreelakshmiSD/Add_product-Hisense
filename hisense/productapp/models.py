from django.db import models

# Create your models here.
ACTIVE_YES_NO_CHOICES = ((None, ''), (True, 'Yes'), (False, 'No'))



class Country(models.Model):
    name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField("Active",default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField("Active",default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    country = models.ForeignKey(Country,on_delete =models.CASCADE)



    def __str__(self):
        return self.name
    
class ScreenSize(models.Model):
    screensize = models.CharField(blank=True)
    is_active = models.BooleanField("Active",default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class Sku_Classification(models.Model):
    name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField("Active",default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name
    
class Division(models.Model):
    name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField("Active",default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    sku_classification = models.ForeignKey(Sku_Classification,on_delete =models.CASCADE)
    screen = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField("Active",default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    division = models.ForeignKey(Division,on_delete =models.CASCADE)


    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField("Active",default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    division = models.ForeignKey(Division,on_delete =models.CASCADE)



    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField("Active",default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    category = models.ForeignKey(Category,on_delete =models.CASCADE)

    def __str__(self):
        return self.name
    


    




