from django.shortcuts import render, redirect
from .models import Requests,Employee,Events,CustomUser,Company
from .forms import RequestForm,LoginForm,RegisterEmployeeForm
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404



def employee_navbar(request):
    return render(request, 'vacayvue/employee_navbar.html')

def company_navbar(request):
    return render(request, 'vacayvue/company_navbar.html')

def calendar(request):  
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'vacayvue/calendar.html',context)
 
def all_events(request):                                                                                                 
    all_events = Events.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name, 
            'id':event.id,                                                                                                                                                                                      
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 

def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)
 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)
 

def list_requests(request):
    all_requests=Requests.objects.all()
    return render(request, 'vacayvue/list-requests.html',
        { 'all_requests':all_requests})

def add_request(request):
    submitted = False
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add-request/?submitted=True')
    else:
        form = RequestForm()  # Using the updated RequestForm
    if 'submitted' in request.GET and request.GET['submitted'] == 'True':
        submitted = True
    return render(request, 'vacayvue/add-request.html', {'form': form, 'submitted': submitted})




def list_employees(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    employees = company.employees.all()
    return render(request, 'vacayvue/list_employees.html', {'company': company, 'employees': employees})


def check_admin_permission(user, company_id):
    # Check if the user is authenticated and is a manager
    if user.is_authenticated and user.user_type == 'admin':
        # Retrieve the company object
        company = get_object_or_404(Company, id=company_id)

        # Verify if the user is associated with the company as a manager
        if Employee.objects.filter(admin=user, company=company).exists():
            # User is authorized
            return True
    return False



def register_employee(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    
    # Check manager permission
    if not check_admin_permission(request.user, company_id):
        return HttpResponseForbidden("You are not authorized to register employees for this company.")
    
    if request.method == 'POST':
        form = RegisterEmployeeForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'employee'
            user.save()
            # Associate the user with the company
            Employee.objects.create(
                adminm=request.user,  # Assuming the current user is the manager
                company=company,
                join_date=form.cleaned_data['date_joined'],  # Get the join date from the form
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            messages.success(request, f'The employee {user.email} has been registered!')
            return redirect('list_employees', company_id=company_id)
    else:
        form = RegisterEmployeeForm(initial={'company': company})
    
    return render(request, 'vacayvue/register_employee.html', {'form': form})


def employee_home(request):
    employee = request.user.employee  # Directly access employee object
    company = employee.company  # Retrieve associated company
    return render(request, 'vacayvue/employee_home.html', {'employee': employee, 'company': company})



def company_home(request, company_id):
    print("Request user:", request.user)
    print("Is user authenticated:", request.user.is_authenticated)
    print("User type:", request.user.user_type) 
    print(f"Company home view accessed with company_id: {company_id}")
    company = get_object_or_404(Company, id=company_id)
    print(f"Retrieved company: {company}")
    employees = company.employees.all()
    print(f"Retrieved employees for company: {employees}")
    return render(request, 'vacayvue/company_home.html', {'company': company, 'employees': employees})




def logout_user(request):
    logout(request)
    messages.success(request, 'Είσαι Αποσυνδεμένος')
    return redirect('main_home')



from django.urls import reverse

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']
            print(f"Attempting user authentication with email: {email}, user_type: {user_type}")
            user = authenticate(request, email=email, password=password)

            if user is not None:
                print("User authentication successful.")
                if user.user_type == 'employee' and user.email == email:
                    login(request, user)
                    print("Redirecting to employee home...")
                    return redirect('employee_home')
                elif user.user_type == 'company' and user.email == email:
                    # Set the company_id in the session data
                    company_id = user.company_profile.id
                    request.session['company_id'] = company_id
                    print(f"Company login successful. Redirecting to company home with company_id: {company_id}")
                    return redirect('company_home', company_id=company_id)
                else:
                    messages.error(request, 'Invalid email or user type.')
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Invalid form data.')
    else:
        form = LoginForm()
    return render(request, 'vacayvue/login.html', {'form': form})







def main_home(request):
    #Get current year 
    company = login_user(request)  # Replace with your logic to get the current company
    
    current_year=datetime.now().year
    return render(request, 'vacayvue/main_home.html', {'company': company, 'current_year':current_year,})  
       
        
    







