from django.db import models

# Create your models here.
class Customer(models.Model):
    FirstName = models.TextField()
    SecondName = models.TextField()
    CompanyName = models.TextField()
    GstTax = models.IntegerField(null=True,)
    def __str__(self):
        return self.FirstName
class Address(models.Model):
    FirstAddress = models.CharField(max_length=500)
    ScondAddress = models.CharField(max_length=500)
    customer   = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.FirstAddress   
class Contacts(models.Model):
    MobileNumber = models.IntegerField()
    EmailId = models.EmailField()
    Position = models.TextField(max_length=100)
    customer   = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True)


