# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     # name=models.CharField(null=False,max_length=50)
#     is_buyer=models.BooleanField(default=False)
#     is_seller=models.BooleanField(default=False)
#     address =models.TextField(null=True)

#     # def __str__(self):
#     #     return self.
    
#     class Meta:
#         db_table='User'


# class Owner():
#     firstname=models.CharField(max_length=50)
#     lastname=models.CharField(max_length=50)
#     Email=models.EmailField(max_length=254)
#     password=models.CharField(max_length=50)
#     address=models.CharField(max_length=50)

#     def __str__(self):
#         return self.firstname

#     class Meta:
#         db_table='owner'
    
# # Create your models here.
# # class User():
# #     firstname=models.CharField(max_length=50)
# #     lastname=models.CharField(max_length=50)
# #     Email=models.EmailField(max_length=254)
# #     password=models.CharField(max_length=50)
# #     address=models.CharField(max_length=50)

# #     def __str__(self):
# #         return self.firstname

# #     class Meta:
# #         db_table='user'




# # class BuyerDetail():
# #     firstname=models.CharField(max_length=50)
# #     lastname=models.CharField(max_length=50)
# #     Email=models.EmailField(max_length=254)
# #     password=models.CharField(max_length=50)
# #     address=models.CharField(max_length=50)

# #     def __str__(self):
# #         return self.firstname

# #     class Meta:
# #         db_table='owner'

# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     vendor=models.BooleanField(default=False)
#     customer=models.BooleanField(default=False)
#     contactnum=models.CharField(max_length=15)
#     gender=models.CharField(max_length=1)
#     createdAt=models.DateField

#     class Meta:
#         db_table='user'
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # name=models.CharField(null=False,max_length=50)
    is_buyer=models.BooleanField(default=False)
    is_seller=models.BooleanField(default=False)
    address =models.TextField(null=True)

    # def _str_(self):
    #     return self.
    
    class Meta:
        db_table='User'