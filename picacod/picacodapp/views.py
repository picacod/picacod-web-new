from django.conf import settings
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from picacodapp.models import Applications, Jobs
from django.contrib.auth import logout as auth_logout 
# Create your views here.


def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')

def careers(request):
    jobs=Jobs.objects.all().order_by('-id')
    return render(request,'careers.html',{'jobs':jobs})


def php(request):
    return render(request,'services/php.html')


def wordpress(request):
    return render(request,'services/wordpress.html')


def laravel(request):
    return render(request,'services/laravel.html')


def react(request):
    return render(request,'services/react.html')


def angular(request):
    return render(request,'services/angular.html')


def nodejs(request):
    return render(request,'services/nodejs.html')


def cakephp(request):
    return render(request,'services/cakephp.html')


def codeigniter(request):
    return render(request,'services/codeigniter.html')


def python(request):
    return render(request,'services/python.html')


def django(request):
    return render(request,'services/django.html')


def android(request):
    return render(request,'services/android.html')

def ios(request):
    return render(request,'services/ios.html')


def hybrid(request):
    return render(request,'services/hybrid.html')


def flutter(request):
    return render(request,'services/flutter.html')


def woocommerce(request):
    return render(request,'services/woocommerce.html')


def shopify(request):
    return render(request,'services/shopify.html')


def chatgpt_solution(request):
    return render(request,'services/chatgpt-solution.html')


def contact_center_solutions(request):
    return render(request,'services/contact-center-solutions.html')


def text_to_speech(request):
    return render(request,'services/text-to-speech.html')


def bussiness_intelligence(request):
    return render(request,'services/bussiness-intelligence.html')


def sentimental_intelligence(request):
    return render(request,'services/sentimental-intelligence.html')


def database_management_administrtion(request):
    return render(request,'services/database-management-administrtion.html')


def devops_infrastructure(request):
    return render(request,'services/devops-infrastructure.html')


def information_security_compliance(request):
    return render(request,'services/information-security-compliance.html')


def network_system_administration(request):
    return render(request,'services/network-system-administration.html')


def server_management(request):
    return render(request,'services/server-management.html')


def qa_testing(request):
    return render(request,'services/qa-testing.html')


def portfolio(request):
    return render(request,'portfolio.html')


def contact(request):
    return render(request,'contact.html')


def software_development(request):
    return render(request,'services/software-development.html')


def web_development(request):
    return render(request,'services/web-development.html')


def app_development(request):
    return render(request,'services/app-development.html')


def ai_and_ml(request):
    return render(request,'services/ai-and-ml.html')


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:  
            login(request, user)
            return redirect('adminindex') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request,'admin/login.html')


def adminindex(request):
    openings=Jobs.objects.all().count()
    applications=Applications.objects.all().count()
    return render(request,'admin/index.html',{'openings':openings, 'applications':applications})


def message(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')  
            message = request.POST.get('message')

            email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

            send_mail(
                subject='New Contact Form Message',
                message=email_message,              
                from_email=settings.DEFAULT_FROM_EMAIL,  
                recipient_list=['abc@gmail.com'],   
                fail_silently=False,                
            )
        return render(request,'contact.html')



def add_job(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        skills = request.POST.get('skills')
        vaccancy = request.POST.get('vaccancy')
        minexperience = request.POST.get('minexperience')
        maxexperience = request.POST.get('maxexperience')
        
        Jobs.objects.create(
            title=title,
            skills=skills,
            no_of_vaccancies=vaccancy,
            min_experience=minexperience,
            max_experience=maxexperience
        )
        
        messages.success(request, 'Job added successfully!')
    return render(request,'admin/addjobs.html')


def view_job(request):
    jobs=Jobs.objects.all().order_by('-id')
    return render(request,'admin/viewjobs.html',{'jobs':jobs})


def delete_job(request,job_id):
    job=Jobs.objects.get(id=job_id)
    job.delete()
    return redirect('view_job')


def edit_job(request,job_id):
    job = Jobs.objects.get(id=job_id)
    
    if request.method == 'POST':
        job.title = request.POST['title']
        job.skills = request.POST['skills']
        job.no_of_vaccancies = request.POST['no_of_vacancies']
        job.min_experience = request.POST['minexperience']
        job.max_experience = request.POST['maxexperience']
        
        job.save()  
        
        messages.success(request, 'Job updated successfully!')
    return redirect('view_job')


def apply(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        designation = request.POST.get('designation')
        message = request.POST.get('message')

        if request.FILES.get('resume'):
            resume = request.FILES['resume']
            fs = FileSystemStorage()
            resume_name = fs.save(resume.name, resume)
            resume_url = fs.url(resume_name)
        else:
            resume_url = None  
        
        Applications.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            designation=designation,
            message=message,
            resume=resume_url
        )
    return redirect('careers')


def applications(request):
    applications=Applications.objects.all()
    return render(request,'admin/viewApplications.html',{'applications':applications})


def delete_application(request,application_id):
    application=Applications.objects.get(id=application_id)
    application.delete()
    return redirect('applications')


def logout(request):
    auth_logout(request) 
    return redirect('adminlogin')