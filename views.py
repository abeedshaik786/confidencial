from django.shortcuts import render
from .models import Customer,Address,Contacts
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
import json

# Create your views here.
def customer_rigistration(request):
        subject = Customer.objects.all()
        return render(request,'customer-listview.html',{'subject':subject})
def customer_view(request, customer_id):
        cust_obj = Customer.objects.filter(id=customer_id).first()
        add_obj=None
        concat_obj = None
        if cust_obj:
                add_obj = Address.objects.filter(customer=cust_obj)
                concat_obj = Contacts.objects.filter(customer=cust_obj)
        return render(request,'customer.html',{
                'cust_obj':cust_obj,
                'add_obj':add_obj
                })
        
def customer_saving(request):
        try:
                if request.method =='POST':
                        product_id = request.POST.get("subject")   
                        firstname = request.POST.get('firstname')
                        secondname = request.POST.get('secondname')
                        companyname = request.POST.get('companyname')
                        gsttax = request.POST.get('gsttax')
                        if product_id:
                                obj=Customer.objects.get(id = product_id)
                        else:
                                obj = Customer()
                        obj.FirstName=firstname,
                        obj.SecondName=secondname,
                        obj.CompanyName=companyname,
                        obj.GstTax=gsttax
                        obj.save()
                        subject = Customer.objects.all()
                        return render(request,'customer-listview.html',{'subject':subject})
        except(ValueError):
                return HttpResponse("<html><body bgcolor=red><h1 style=text-align:center;>invalid data</h1></body></html>")
@csrf_protect
def Customer_Edite(request):
        import pdb;pdb.set_trace    
        if request.method == 'POST':
                # "| print(request.POST) |" this is for debuging purpose that data is to the view or not
                customer_id = request.POST.get('customer_id')
                firstname = request.POST.get('firstname')
                secondname = request.POST.get('secondname')
                companyname = request.POST.get('companyname')
                gsttax = request.POST.get('gsttax')
                obj = Customer.objects.get(id = customer_id)
                obj.FirstName=firstname
                obj.SecondName=secondname
                obj.CompanyName=companyname
                obj.GstTax=gsttax
                obj.save()
                response_data = serializers.serialize('json', Customer.objects.fillter(id = customer_id ))
                return JsonResponse(response_data,safe=False)
                # return HttpResponseRedirect(reverse('Customer:customer_view', args={cust_obj.id}))

def Address_saving(request):
        print(request.POST)
        if request.method=="POST":
                import pdb;pdb.set_trace   
                customer_id = request.POST.get('customer_id')
                firstaddress = request.POST.get('firstaddress')
                secondaddress = request.POST.get('secondaddress')
                cust_obj=Customer.objects.get(id=customer_id)
                subj= Address() 
                subj.FirstAddress=firstaddress
                subj.ScondAddress=secondaddress
                subj.customer=cust_obj
                subj.save()
                # Address_data = serializers.serialize('json', Customer.objects.filter( id = customer_id ))
                # print(Address_data)
                return JsonResponse({'success':True})
        #subject = Address.objects.all()
        #return HttpResponseRedirect(reverse('Customer:customer_view', args={ cust_obj.id }))
       # return redirct("{% url 'customer:customer_view' customer_id=%s %}")
       # return render(request,'designe.html',{'Address_data':subject })
def Address_Edite(request):
        address = request.GET.get('address_id')
        data = serializers.serialize('json', Address.objects.filter(id = address))
        return JsonResponse(data,safe=False)
def Address_Edite_Saving(request):
        if request.method=="POST":
                address_id = request.POST.get('Address_id') 
                customer_id = request.POST.get('customer_id')
                firstaddress = request.POST.get('firstaddress')
                secondaddress = request.POST.get('secondaddress')
                cust_obj = Customer.objects.get(id=customer_id)
                sub= Address.objects.get(id=address_id)
                # sub= Address() 
                sub.FirstAddress=firstaddress
                sub.ScondAddress=secondaddress
                # sub.costomer=cust_obj
                sub.save()
                return HttpResponseRedirect(reverse('Customer:customer_view', args={ cust_obj.id }))
                #subject = Address.objects.all()
        # return render(request,'designe.html')
def Contacts_Edite_Saving(request):
        if request.method == "POST":
                contacts_id = request.POST.get('contacts_id')
                customer_id = request.POST.get('customer_id')
                MobileNumber = request.POST.get('mobilenumber')
                EmailId = request.POST.get('email')
                Position = request.POST.get('position')
                cust_obj = Customer.objects.get(id = customer_id)
                cobj = Contacts.objects.get( id = contacts_id)
                cobj.MobileNumber = MobileNumber
                cobj.EmailId = EmailId
                cobj.Position = Position
                cobj.save()
                return HttpResponseRedirect(reverse('Customer:customer_view', args={ cust_obj.id}))

def Contacts_Edite(request):
        import pdb;pdb.set_trace    
        contacts = request.GET.get('contact_id')
        data=serializers.serialize('json',Contacts.objects.filter(id = contacts))
        return JsonResponse(data,safe=False)
def Contacts_saving(request):
        import pdb;pdb.set_trace    
        customer_id = request.POST.get('customer_id')
        MobileNumber = request.POST.get('mobilenumber')
        EmailId = request.POST.get('email')
        Position = request.POST.get('position')
        cust_obj = Customer.objects.get(id=customer_id)
        cobj = Contacts()
        cobj.MobileNumber=MobileNumber
        cobj.EmailId=EmailId
        cobj.Position=Position
        cobj.customer=cust_obj
        cobj.save()
        #subjecte = Address.objects.all()
        return HttpResponseRedirect(reverse('Customer:customer_view', args={ cust_obj.id }))
       # return render(request,'home.html',{'Con_subject':subjecte})
def customer_Delete(request,idd):
        obj = Customer.objects.get(id = idd)
        obj.delete()
        subject = Customer.objects.all()
        return render(request,'customer-listview.html',{'subject':subject})
def Address_Delete(request,idd):
        obj = Address.objects.get(id=idd)
        obj.delete()
        return render(request,'customer.html')




