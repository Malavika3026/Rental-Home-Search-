from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from.models import Home_Property,Booking
# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=="POST":
        fn=request.POST['fname']
        ln=request.POST['lname']
        un=request.POST['uname']
        c=request.POST['contact']
        e=request.POST['em']
        ps=request.POST['psw']
        if User.objects.filter(username=un).exists():
            messages.info(request,"Username Exists")
            return render(request,"register.html")
        elif User.objects.filter(email=e).exists():
            messages.info(request,"Email Exists")
            return render(request,"register.html")
        else:
            #Store the value in database
            #Create object for database name
            user=User.objects.create_user(first_name=fn,last_name=ln,email=e,password=ps,username=un)
            user.save()
            return redirect('login')
    else:
        return render(request,"register.html")
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        un=request.POST['uname']
        ps=request.POST['psw']
        user=auth.authenticate(username=un,password=ps)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,"login.html")

    return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def explore(request):
    hp=Home_Property.objects.all()
    return render(request,"explore.html",{"explore":hp})



def adminlogin(request):
    if request.method=="POST":
        un=request.POST['uname']
        ps=request.POST['psw']
        user=auth.authenticate(username=un,password=ps)
        if user is not None and user.is_superuser:

            auth.login(request,user)
            return redirect('adminhome')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,"adminlogin.html")
    return render(request,"adminlogin.html")

def add(request):
    if request.method == "POST" and request.FILES:
        action = request.POST.get('action')

        if action == "save":
            # Save logic
            t = request.POST['title']
            d = request.POST['des']
            
            max_price = request.POST['pmax']
            c = request.POST['cat']
            imgm = request.FILES.get('main')
            imgp = request.FILES.get('person')
            l = request.POST['loc']
            
            m = Home_Property.objects.create(
                title=t,
                description=d,
                
                price_max=max_price,
                category=c,
                image_main=imgm,
                image_person=imgp,
                location=l
            )
            m.save()
            messages.info(request,"Successfully Added")
            return redirect('explore')

        elif action == "delete":
            # Example delete logic: delete based on title (not recommended for production)
            title = request.POST['title']
            Home_Property.objects.filter(title=title).delete()
            return redirect('adminhome')

    return render(request, "add.html")


def adminhome(request):
    return render(request,"adminhome.html")

def booking(request, property_id):
    property_obj = get_object_or_404(Home_Property, id=property_id)

    if request.method == 'POST':
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        notes = request.POST.get('notes', '')

        # Set amount based on property price (e.g., price_min)
        amount = property_obj.price_max  # or price_max, or calculate based on duration

        if check_in and check_out:
            booking = Booking.objects.create(
                user=request.user,
                property=property_obj,
                check_in=check_in,
                check_out=check_out,
                notes=notes,
                amount=amount
            )
            messages.success(request, "Booking successful! Proceed to payment.")
            return redirect('payment', booking_id=booking.id)
        else:
            messages.error(request, "Please provide both check-in and check-out dates.")

    return render(request, "booking.html", {'property': property_obj})




def payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        # Simulate successful payment (or integrate a real payment gateway)
        booking.status = 'Paid'
        booking.save()

        messages.success(request, "Payment Successful! Your booking is confirmed.")
        return render(request, 'payment_success.html', {'booking': booking})

    return render(request, "payment.html", {'booking': booking})