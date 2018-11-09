from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from proprietor.models import Property,Profile,Tenant

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail

from datetime import datetime,timedelta
from django.utils import timezone
from datetime import datetime

from django.utils.dateparse import parse_date
# Create your views here.


def home(request):
	return render(request, "home.html")

def owner(request):
	user = request.user
	name= user.username
	# if Property.objects.owner==user:
	myproperty = Property.objects.filter(owner=user)
	print(myproperty)
	# return render(request,"property_details.html",{'myproperty':myproperty})

	return render(request, "owner_site.html",{'myproperty':myproperty,'name':name})


def tenant(request):
	user =request.user
	name= user.username
	print(name)
	myproperty = Tenant.objects.filter(user=user)
	print(myproperty)
	return render(request, "tenant_site.html",{'name':name,'myproperty':myproperty})

def contact(request):
	return render(request, "contact.html")


def about(request):
	return render(request, "about.html")

def faq(request):
	return render(request, "faq.html")

def signin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		# users = request.POST.get('users')
		user = authenticate(request, username=username, 
			password=password)
		if user is not None:
			login(request, user)


			users = Profile.objects.get(username=username)
			utype = users.choice

			print(utype)

			if utype == "O":
				# return render(request, "owner_site.html")
				return redirect('owner_site')

			else:
				# return HttpResponse(users)
				# return render(request, "tenant_site.html")
				return redirect('tenant_site')
			# return HttpResponse("Success!")
		else:
			return HttpResponse("Please check info")
	return render(request, "signin.html")





def signup(request):
	if request.method =="POST":
		username = request.POST.get('username',None)
		email = request.POST.get('email')
		password = request.POST.get('password',None)
		# firstname = request.POST.get('firstname')
		# lastname = request.POST.get('lastname')
		users = request.POST.get("users")

		try:
			user = User.objects.get(username=username)
			
		except:
			user=None

		if user is None:
			user = User.objects.create_user(username, email, password)
			user_details = Profile(user=user,choice=users,email=email,username=username)
			user_details.save()


			return redirect('login')

			
		else :
			return HttpResponse("Please check info, User may already exists")
	return render(request, "signup.html")





def del_prop(request):
	if request.method =="POST":
		# propname = request.POST.get('name')
		# prop = Property.objects.get(name=propname)
		pid = request.POST.get('property_id')
		propt = Property.objects.get(pk=pid)

		propt.delete()

		return redirect("owner_site")

	user = request.user
	prop = Property.objects.filter(owner=user)
	name= user.username

	return render(request,"del_prop.html",{'property':prop , "name":name}) 

	


def property_details(request):
	user = request.user
	# if Property.objects.owner==user:
	myproperty = Property.objects.filter(owner=user)
	print(myproperty)
	return render(request,"property_details.html",{'myproperty':myproperty})

def tenant_details(request):
	owner = request.user
	properties = Property.objects.filter(owner=owner)
	tenants = []

	name= owner.username
	for prop in properties:
		try:
			tenant = Tenant.objects.get(prop=prop)
			tenants.append(tenant)
		except:
			pass
	print(tenants)
	return render(request,"tenant_details.html",{"tenants":tenants,"name":name})



def add_property(request):
	if request.method == "POST":
		name = request.POST.get('name')
		address = request.POST.get('address')

		user = request.user
		title = Property(name=name,address=address,owner=user)
		title.save()
		
		
		return redirect('owner_site')
	
	user = request.user
	name= user.username	
	return render(request, 'add_prop.html',{"name":name})


def add_tenant(request):
	if request.method == "POST":
		
		user = request.user
		
		email = request.POST.get('email')
		prop_name = request.POST.get('property')

		
		tenant = User.objects.get(email=email)
		print(tenant)

		date = request.POST.get('rent')
		pid = request.POST.get('property_id')
		propt = Property.objects.get(pk=pid)
		date_int = parse_date(date)
		tdelta = timedelta(days=23)
		d=date_int + tdelta

		info = Tenant(prop=propt,user=tenant,rent_date=date,notify_date=d)
		info.save()




		return redirect("owner_site")

	user = request.user
	properties = Property.objects.filter(owner=user)
	name= user.username


	
	for prop in properties:
		try:
			tenant = Tenant.objects.get(prop=prop)
			# tenants.append(tenant)
			print(tenant.notify_date)

		except:
			pass


	return render(request, 'add_tenant.html',{'property':properties , "name":name})


def rent_reminder(request):
	# user = request.user
	tenants = Tenant.objects.all()

	to =[]
	today = datetime.today()
	for tenant in tenants:
		day = tenant.notify_date
		print(day, today.date())
		if str(day) == str(today.date()):
			to.append(tenant.user.email)

	for email in to:
		a = str(tenant.prop.owner.email)
		data = """
		Hey there!

		Your rent is due in 7 days.

		Log in to pay now!
		https://inframan.herokuapp.com 
		"""
		send_mail('Rent is Due in 7 days',
    			data,
    			a, [email])
	return HttpResponse(f"{to}")

	

		

def logout_user(request):
    logout(request)
    return redirect('home')



def invite(request):
	if request.method == "POST":
		email = request.POST.get('email')
		data = """
	Hello there!

	You have been invited to log into the rental web
	app and manage your rental information.

	Sign Up here!!
	https://inframan.herokuapp.com 

	 Cheers!! :)
	 ~ Nisha
	     """
		send_mail('Welcome!', data, "Nisha",[email], fail_silently=False)
		user = request.user
		name= user.username
		return redirect('invite')

	user=request.user
	name=user.username
	return render(request, 'invite.html',{"name":name})






def edit_profile(request):
	user = request.user

	name= user.username
	# profile = Profile.objects.get(user=user)

	pro=get_object_or_404(Profile, user=user)
	print(pro)

	if request.method == "POST":

		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		# name = request.POST.get('username')
		# dob = request.POST.get('dob')
		email = request.POST.get('email')
		no = request.POST.get('no')
		
		# pro.username=name
		pro.email=email
		pro.phone_number = no 
		pro.first_name = firstname
		pro.last_name = lastname
		# pro.dob = dob
		pro.save()

		return redirect('edit_profile')


	return render(request, 'edit_profile.html', {'profile': pro ,"name":name})


def edit_profile_tenant(request):
	user = request.user

	name= user.username
	# profile = Profile.objects.get(user=user)

	pro=get_object_or_404(Profile, user=user)
	print(pro)

	if request.method == "POST":

		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		name = request.POST.get('username')
		# dob = request.POST.get('dob')
		# email = request.POST.get('email')
		no = request.POST.get('no')
		
		pro.username=name
		# pro.email=email
		pro.phone_number = no 
		pro.first_name = firstname
		pro.last_name = lastname
		# pro.dob = dob
		pro.save()

		return redirect('edit_profile_tenant')
	


	return render(request, 'edit_profile_tenant.html', {'profile': pro ,"name":name})


	
# def send(self):
#     subject = u'Invitation to join Django Bookmarks'
#     link = 'http://%s/friend/accept/%s/' % (
#       settings.SITE_HOST,
#       self.code
#     )
#     template = get_template('invitation_email.txt')
#     context = Context({
#       'name': self.name,
#       'link': link,
#       'sender': self.sender.username,
#     })
#     message = template.render(context)
#     send_mail(
#       subject, message,
#       settings.DEFAULT_FROM_EMAIL, [self.email]    )

