from django.db import models

# Create your models here.

class PropertyType(models.Model):
    name=models.CharField(max_length=50)


    def _str_(self):
        return self.name
    
    class Meta:
        db_table='propertyType'   



class propertyDetail(models.Model):
    name=models.CharField(max_length=50)
    constructionyear=models.DateField(auto_now=False,auto_now_add=False)
    buildrname=models.CharField(max_length=50)
    rera=models.BooleanField(default=True)

    def _str_(self):
        return self.name
    
    class Meta:
        db_table='propertyDetail'        


class property(models.Model):
    propertyDetail=models.ForeignKey(propertyDetail,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    rent=models.BooleanField(default=True)