from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from datetime import  datetime
from django.shortcuts import get_object_or_404
from .models import User

import base64

mediapath = "C:\\22-23\\trendtrove\\media\\"


from myapp.models import *


def login(request):

    request.session["lid"]=""

    return render(request, "admins/login.html")

def log_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    var=Login.objects.filter(username=username,password=password)
    if var.exists():
        var1 = Login.objects.get(username=username, password=password)
        request.session['lid']=var1.id
        if var1.type=='admin':
            return redirect('/myapp/admins_home/')
        elif var1.type=='driver':
            return redirect('/myapp/driverhome/')
        elif var1.type=='user':
            return redirect('/myapp/uhome/')
        else:
            return HttpResponse('''<script>alert("No user found. Invalid username or password");window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse('''<script>alert("No user found. Invalid username or password");window.location="/myapp/login/"</script>''')



def home(request):

    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:

        return render(request, "admins/home.html")




def admins_add_driver(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request, "admins/add_driver.html")
def admins_add_driver_post(request):
    name= request.POST["textfield"]
    gender= request.POST["select"]
    housename= request.POST["textfield2"]
    place= request.POST["textfield3"]
    city= request.POST["textfield4"]
    state= request.POST["textfield5"]
    email= request.POST["textfield6"]
    phone= request.POST["textfield7"]
    file= request.FILES["fileField"]
    import random

    fs= FileSystemStorage()
    from datetime import  datetime
    filename= datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    fs.save(filename,file)

    l=Login()
    l.username= email
    l.password = str(random.randint(1000000,900000000))
    l.type="driver"
    l.save()

    cobj=Driver()
    cobj.name=name
    cobj.gender= gender
    cobj.housename=housename
    cobj.place=place
    cobj.email=email
    cobj.city= city
    cobj.state=state
    cobj.phone=phone
    cobj.LOGIN=l
    cobj.photo= fs.url(filename)
    cobj.save()

    return HttpResponse("<script>alert('Driver added successfully');window.location='/myapp/admins_add_driver/'</script>")
def admins_view_driver(request):

    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        cl = Driver.objects.all()

        return render(request, "admins/Viewdriver.html", {'data': cl})
def admins_view_driver_post(request):

    s=request.POST["textfield"]
    cl = Driver.objects.filter(name__icontains=s)

    return render(request, "admins/Viewdriver.html", {'data': cl})
def admins_delete_driver(request, id):
    Driver.objects.get(id=id).delete()

    return HttpResponse("<script>alert('Driver  deleted successfully');window.location='/myapp/admins_view_driver/'</script>")
def admins_edit_driver(request, id):
    c=Driver.objects.get(id=id)

    return render(request, "admins/edit_driver.html", {'data': c})
def admins_edit_driver_post(request):
    id = request.POST["id"]
    name = request.POST["textfield"]
    gender = request.POST["select"]
    housename = request.POST["textfield2"]
    place = request.POST["textfield3"]
    city = request.POST["textfield4"]
    state = request.POST["textfield5"]
    email = request.POST["textfield6"]
    phone = request.POST["textfield7"]

    cobj = Driver.objects.get(id=id)
    cobj.name = name
    cobj.gender = gender
    cobj.housename = housename
    cobj.place = place
    cobj.email = email
    cobj.city = city
    cobj.state = state
    cobj.phone = phone

    if 'fileField' in request.FILES:
        import random
        file = request.FILES["fileField"]
        fs = FileSystemStorage()
        from datetime import datetime
        filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        fs.save(filename, file)
        cobj.photo = fs.url(filename)

    cobj.save()

    return HttpResponse("<script>alert('Clerk added successfully');window.location='/myapp/admins_view_driver/'</script>")



def admin_addvehicle(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return  render(request,"admins/add_vehicle.html")

def admin_addvehicle_post(request):
    regno= request.POST["textfield"]
    model= request.POST["textfield1"]
    engineno= request.POST["textfield2"]
    totalseat= request.POST["textfield3"]
    ac= request.POST["select"]
    vehicletype= request.POST["select2"]
    file= request.FILES["file"]




    v=Vehicle()
    v.vehicleregno= regno
    v.vehiclemodel= model
    v.enginenumber= engineno
    v.ac_nonac=ac
    v.totalseats= totalseat
    v.vehicletype= vehicletype
    fs = FileSystemStorage()
    from datetime import datetime
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    fs.save(filename, file)


    v.photo= fs.url(filename)

    file1 = request.FILES["file1"]
    fs = FileSystemStorage()
    from datetime import datetime
    filename = "fff" + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    fs.save(filename, file1)

    v.rcfile= fs.url(filename)
    v.save()
    return  HttpResponse("<script>alert('Vehicle added successfully');window.location='/myapp/admin_addvehicle/'</script>")

def admin_view_vehicle(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        allveh= Vehicle.objects.all()
        return render(request,"admins/Viewvehicle.html",{'data': allveh})

def admin_view_vehicle_post(request):
    s=request.POST["textfield"]
    allveh= Vehicle.objects.filter(vehicleregno__icontains=s)
    return render(request,"admins/Viewvehicle.html",{'data': allveh})

def admin_delete_vehicles(request,vid):
    Vehicle.objects.filter(id=vid).delete()
    return HttpResponse(
        "<script>alert('Vehicle delete successfully');window.location='/myapp/admin_view_vehicle/'</script>")

def admin_edit_vehicles(request,id):
    s= Vehicle.objects.get(id=id)
    return render(request, "admins/edit_vehicle.html", {'data': s})


def admin_editvehicle_post(request):
    id= request.POST["id"]
    regno= request.POST["textfield"]
    model= request.POST["textfield1"]
    engineno= request.POST["textfield2"]
    totalseat= request.POST["textfield3"]
    ac= request.POST["select"]
    vehicletype= request.POST["select2"]


    v=Vehicle.objects.get(id=id)
    v.vehicleregno= regno
    v.vehiclemodel= model
    v.enginenumber= engineno
    v.ac_nonac=ac
    v.totalseats= totalseat
    v.vehicletype= vehicletype

    if 'file' in request.FILES:

        file = request.FILES["file"]
        fs = FileSystemStorage()
        from datetime import datetime
        filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        fs.save(filename, file)
        v.photo= fs.url(filename)
    v.save()
    return  HttpResponse("<script>alert('Vehicle edietd successfully');window.location='/myapp/admin_view_vehicle/'</script>")


def admins_view_complaints(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        c=Complaint.objects.all()
        return render(request, "admins/Viewcomplaint.html", {'data': c})



def admins_view_complaints_post(request):
    f=request.POST["f"]
    t=request.POST["t"]
    c = Complaint.objects.filter(date__range=[f,t])
    return render(request, "admins/Viewcomplaint.html", {'data': c})

def admins_sent_reply(request,id):
    return render(request,"admins/sentreply.html",{'id':id})

def admins_sent_reply_post(request):
    id= request.POST["id"]
    reply= request.POST["reply"]
    c=Complaint.objects.get(id=id)
    c.reply= reply
    c.status="replied"
    c.save()
    return HttpResponse("<script>alert('Replied successfully');window.location='/myapp/admins_view_complaints/'</script>")



def admin_change_password(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request, "admins/change password.html")

def admin_changepas_post(request):
    currentpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    res=Login.objects.filter(password=currentpassword,id=request.session['lid'])
    if res.exists():
        res1 = Login.objects.get(password=currentpassword, id=request.session['lid'])
        if newpassword==confirmpassword:
            res2 = Login.objects.filter(password=currentpassword, id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert("Changed Successfully");window.location="/myapp/login/"</script>''')
        else :
            return HttpResponse('''<script>alert("Password mismatch");window.location="/myapp/login/"</script>''')
    else :
        return HttpResponse('''<script>alert("Invalid password. Please try again");window.location="/myapp/login/"</script>''')


def admin_car_driver_assign(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:

        v=Vehicle.objects.all()
        s=[]

        for i in v:

            if not Carassign.objects.filter(VEHICLE=i).exists():
                s.append(i)

        v=s



        d=Driver.objects.all()
        s = []
        for i in d:
            if not Carassign.objects.filter(DRIVER=i).exists():
                s.append(i)

        d=s





        return render(request,"admins/car_assign.html",{ 'v':v, 'd':d })





def admin_car_driver_assign_post(request):
    car= request.POST["car"]
    driver= request.POST["driver"]

    c=Carassign()
    c.VEHICLE_id= car
    c.DRIVER_id=driver
    c.save()

    return HttpResponse("<script>alert('Car Assigned successfully');window.location='/myapp/admin_car_driver_assign/'</script>")



def admin_view_car_driver_assign(request):

    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        a=Carassign.objects.all()

        return render(request,"admins/viewcar_driver_assign.html", {'data': a})




def admin_view_car_driver_assign_post(request):
    a=Carassign.objects.filter()

    return render(request,"admins/viewcar_driver_assign.html", {'data': a})



def admin_delete_car_assign(request,id):

    Carassign.objects.filter(id=id).delete()
    return HttpResponse(
        "<script>alert('Assignment deleted successfully');window.location='/myapp/admin_view_car_driver_assign/'</script>")


def admin_view_users(request):

    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        u=User.objects.all()

        return  render(request,"admins/Viewuser.html",{'data': u})


def admin_view_users_post(request):


    name= request.POST["textfield"]

    u=User.objects.filter(name__icontains=name)

    return  render(request,"admins/Viewuser.html",{'data': u})



##################user portion

def uhome(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request,"user/home.html")

def user_signup(request):
    return render(request, "user/signup.html")

def user_signup_post(request):
    name = request.POST["textfield"]
    gender = request.POST["select"]
    housename = request.POST["textfield2"]
    place = request.POST["textfield3"]
    city = request.POST["textfield4"]
    state = request.POST["textfield5"]
    email = request.POST["textfield6"]
    phone = request.POST["textfield7"]

    password = request.POST["textfield10"]
    file = request.FILES["fileField"]
    fs = FileSystemStorage()
    from datetime import datetime
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    fs.save(filename, file)
    l = Login()
    l.username = email
    l.password= password
    l.type = "user"
    l.save()

    cobj = User()
    cobj.name = name
    cobj.gender = gender
    cobj.housename = housename
    cobj.place = place
    cobj.email = email
    cobj.city = city
    cobj.state = state
    cobj.phone = phone
    cobj.LOGIN = l
    cobj.photo = fs.url(filename)

    cobj.save()

    return HttpResponse("<script>alert('Account created successfully');window.location='/myapp/login/'</script>")













def user_view_profile(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')
    else:
        u = User.objects.get(LOGIN__id=request.session['lid'])
        return render(request, "user/viewprofile.html", {'u': u})


def user_edit_profile(request):
    u = User.objects.get(LOGIN_id=request.session['lid'])
    return render(request, "user/editprofile.html", {'data': u})



def user_editprofile_post(request):
    name = request.POST["textfield"]
    gender = request.POST["select"]
    housename = request.POST["textfield2"]
    place = request.POST["textfield3"]
    city = request.POST["textfield4"]
    state = request.POST["textfield5"]
    email = request.POST["textfield6"]
    phone = request.POST["textfield7"]


    cobj = User.objects.get(LOGIN_id=request.session['lid'])
    cobj.name = name
    cobj.gender = gender
    cobj.housename = housename
    cobj.place = place
    cobj.email = email
    cobj.city = city
    cobj.state = state
    cobj.phone = phone

    if 'fileField' in request.FILES:
        file = request.FILES["fileField"]

        fs = FileSystemStorage()
        from datetime import datetime
        filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        fs.save(filename, file)


    cobj.save()

    return HttpResponse("<script>alert('Account edited successfully');window.location='/myapp/user_view_profile/'</script>")


def user_add_complaint(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request,"user/sentcomplaint.html")
def user_add_complaint_post(request):
    complaint= request.POST["complaint"]

    c=Complaint()
    c.USER= User.objects.get(LOGIN_id= request.session['lid'])
    c.complaint=complaint
    c.reply="pending"
    c.status="pending"
    c.date=datetime.now()
    c.save()





    return HttpResponse("<script>alert('Complaint sent successfully');window.location='/myapp/user_add_complaint/'</script>")




def user_view_complaint(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        fall = Complaint.objects.filter(USER__LOGIN_id= request.session['lid'])
        return render(request, "user/Viewcomplaint.html", {'fall': fall})

def user_view_complaint_post(request):

    f=request.POST["f"]
    t=request.POST["t"]

    fall = Complaint.objects.filter(USER__LOGIN_id= request.session['lid'], date__range=[f,t])
    return render(request, "user/Viewcomplaint.html", {'fall': fall})



def user_view_cabs_post(request):

    totalseats=request.POST["textfield3"]
    vehicletype=request.POST["select2"]
    acstatus=request.POST["select"]

    v=Vehicle.objects.filter(Q(totalseats=totalseats) & Q(vehicletype=vehicletype) & Q(ac_nonac=acstatus))

    return render(request,"user/Viewvehicle.html", {'data': v })



def user_view_cabs(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        v=Vehicle.objects.all()
        return render(request,"user/Viewvehicle.html", {'data': v })


def user_booking(request,vid):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:

        return render(request,"user/booking.html",{'vid':vid})

def user_booking_post(request):
    pickup=request.POST["textfield"]
    drop=request.POST["textfield2"]
    vid=request.POST["vid"]
    # time=request.POST["textfield3"]




    bobj= booking()
    bobj.USER= User.objects.get(LOGIN_id= request.session['lid'])
    bobj.date= datetime.now()
    bobj.pick= pickup
    bobj.drop= drop
    bobj.VEHICLE_id=vid
    bobj.status="booked"
    bobj.time=datetime.now().time().strftime("%H:%M:%S")
    # bobj.time=datetime.now().time()
    bobj.save()

    return HttpResponse("<script>alert('Cab booking done successfully');window.location='/myapp/user_view_cabs/'</script>")







def userpayment(request,bid,totalkm):


    amount= 15 * float(totalkm)



    return render(request,"user/pay.html",{'bid':bid, 'amount': amount})

def userpayment_post(request):
    accnt = request.POST["a"]
    ifsc = request.POST["i"]
    password = request.POST["p"]
    amo = request.POST["am"]
    id = request.POST["id"]

    if bank.objects.filter(accountno=accnt, ifsccode=ifsc, password=password, amount__gt=amo).exists():

        bobj = booking.objects.get(id=id)

        bobj.status = "paid"

        bobj.save()

        return HttpResponse(
            "<script>alert('Payment done successfully');window.location='/myapp/user_view_booking/'</script>")
    else:
        return HttpResponse(
            "<script>alert('Cab booking failed. Please check your account credentials or check balance');window.location='/myapp/user_view_booking/'</script>")


def user_change_password(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request, "user/change password.html")

def user_changepas_post(request):
    currentpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    res = Login.objects.filter(password=currentpassword, id=request.session['lid'])
    if res.exists():
        res1 = Login.objects.get(password=currentpassword, id=request.session['lid'])
        if newpassword == confirmpassword:
            res2 = Login.objects.filter(password=currentpassword, id=request.session['lid']).update(
                password=confirmpassword)
            return HttpResponse(
                '''<script>alert("Changed Successfully");window.location="/myapp/login/"</script>''')
        else:
            return HttpResponse(
                '''<script>alert("Password mismatch");window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert("Invalid password");window.location="/myapp/login/"</script>''')



def user_view_booking(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        res= booking.objects.filter(USER__LOGIN_id= request.session['lid'])

        return  render(request,"user/view_booking.html",{'data': res})




def user_view_booking_post(request):

    f= request.POST["f"]
    t= request.POST["t"]
    res= booking.objects.filter(USER__LOGIN_id= request.session['lid'], date__range=[f,t])

    return  render(request,"user/view_booking.html",{'data': res})







##############driver

def driverhome(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request,"driver/home.html")




def driver_view_profile(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        print(request.session['lid'],"HIHIHIHHIHII")
        u = Driver.objects.get(LOGIN_id=request.session['lid'])
        return render(request, "driver/viewprofile.html", {'u': u})




def driver_view_booking_new(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        s= Carassign.objects.filter(DRIVER__LOGIN_id= request.session['lid'])
        if s.exists():
            s=s[0]
            s=booking.objects.filter(VEHICLE= s.VEHICLE)


            return render(request,"driver/view_booking_new.html", {'data': s})

        else:
            return HttpResponse(
                '''<script>alert("You have no vehicle assigned");window.location="/myapp/driverhome/"</script>''')



def driver_view_booking_new_post(request):

    f=request.POST["f"]
    t=request.POST["t"]
    s= Carassign.objects.filter(DRIVER__LOGIN_id= request.session['lid'])
    if s.exists():
        s=s[0]
        s=booking.objects.filter(VEHICLE= s.VEHICLE, date__range=[f,t])


        return render(request,"driver/view_booking_new.html", {'data': s})

    else:
        return HttpResponse(
            '''<script>alert("You have no vehicle assigned");window.location="/myapp/driverhome/"</script>''')




def driver_picked(request,id):

    b=booking.objects.get(id=id)
    b.status="picked"
    b.save()

    return HttpResponse(
        '''<script>alert("Picked");window.location="/myapp/driver_view_booking_new/"</script>''')



def driver_cancelled(request,id):

    b=booking.objects.get(id=id)
    b.status="cancelled"
    b.save()

    return HttpResponse(
        '''<script>alert("Picked");window.location="/myapp/driver_view_booking_new/"</script>''')



def driver_dropped(request):

    id= request.POST["iid"]
    total= request.POST["total"]

    b=booking.objects.get(id=id)
    b.status="dropped"
    b.total_km= total
    b.save()

    return HttpResponse(
        '''<script>alert("Dropped");window.location="/myapp/driver_view_booking_new/"</script>''')


def driver_change_password(request):
    if request.session["lid"]=="":
        return redirect('/myapp/login/')

    else:
        return render(request, "driver/change password.html")

def driver_changepas_post(request):
    currentpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    res = Login.objects.filter(password=currentpassword, id=request.session['lid'])
    if res.exists():
        res1 = Login.objects.get(password=currentpassword, id=request.session['lid'])
        if newpassword == confirmpassword:
            res2 = Login.objects.filter(password=currentpassword, id=request.session['lid']).update(
                password=confirmpassword)
            return HttpResponse(
                '''<script>alert("Changed Successfully");window.location="/myapp/login/"</script>''')
        else:
            return HttpResponse(
                '''<script>alert("Password mismatch");window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert("Invalid password");window.location="/myapp/login/"</script>''')







# def email_exist(request):
#     email_ex = request.POST['email']
#     if User.objects.filter(email=email_ex).exists():
#         return JsonResponse({'status':'ok'})
#     else:
#         return JsonResponse({'status':'no'})

def forget_password(request):
    return render(request,'forgotpassword.html')

def forget_password_post(request):
    em = request.POST['textfield2']
    import random
    password = random.randint(00000000, 99999999)
    log = Login.objects.filter(username=em)
    if log.exists():
        logg = Login.objects.get(username=em)
        message = 'temporary password is ' + str(password)
        send_mail(
            'temp password',
            message,
            settings.EMAIL_HOST_USER,
            [em, ],
            fail_silently=False
        )
        logg.password = password
        logg.save()
        return HttpResponse('<script>alert("success");window.location="/myapp/login/"</script>')
    else:
        return HttpResponse('<script>alert("invalid email");window.location="/myapp/login/"</script>')


def user_cancelled(request,id):

    b=booking.objects.get(id=id)
    b.status="cancelled"
    b.save()

    return HttpResponse(
        '''<script>alert("Cancelled");window.location="/myapp/user_view_booking/"</script>''')



def raz_pay(request):

    import razorpay

    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    amount = 2000000

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    return render(request, 'user/pp.html',{ 'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id']})



def get_vehicles(request):
    department_id = request.GET.get('department_id')
    datas = Vehicle.objects.filter(vehicletype=department_id)
    data=[]
    for i in datas:
        data.append({
            'vehicleregno':i.vehicleregno,
            'vehiclemodel':i.vehiclemodel,
            'enginenumber':i.enginenumber,
            'totalseats':i.totalseats,
            'ac_nonac':i.ac_nonac,
            'vehicletype':i.vehicletype,
            'photo':i.photo,
            'rcfile':i.rcfile,
            'id':i.id,

        })
    return JsonResponse(data,safe=False)


def sa(request):
    return render(request,"sa.html")