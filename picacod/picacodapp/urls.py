from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('careers/',views.careers,name='careers'),

    path('php/',views.php,name='php'),
    path('wordpress/',views.wordpress,name='wordpress'),
    path('laravel/',views.laravel,name='laravel'),
    path('react/',views.react,name='react'),
    path('angular/',views.angular,name='angular'),
    path('nodejs/',views.nodejs,name='nodejs'),
    path('cakephp/',views.cakephp,name='cakephp'),
    path('codeigniter/',views.codeigniter,name='codeigniter'),
    path('python/',views.python,name='python'),
    path('django/',views.django,name='django'),

    path('android/',views.android,name='android'),
    path('ios/',views.ios,name='ios'),
    path('hybrid/',views.hybrid,name='hybrid'),
    path('flutter/',views.flutter,name='flutter'),

    path('woocommerce/',views.woocommerce,name='woocommerce'),
    path('shopify/',views.shopify,name='shopify'),

    path('chatgpt_solution/',views.chatgpt_solution,name='chatgpt_solution'),
    path('contact_center_solutions/',views.contact_center_solutions,name='contact_center_solutions'),
    path('text_to_speech/',views.text_to_speech,name='text_to_speech'),
    path('bussiness_intelligence/',views.bussiness_intelligence,name='bussiness_intelligence'),
    path('sentimental_intelligence/',views.sentimental_intelligence,name='sentimental_intelligence'),

    path('database_management_administrtion/',views.database_management_administrtion,name='database_management_administrtion'),
    path('devops_infrastructure/',views.devops_infrastructure,name='devops_infrastructure'),
    path('information_security_compliance/',views.information_security_compliance,name='information_security_compliance'),
    path('network_system_administration/',views.network_system_administration,name='network_system_administration'),
    path('server_management/',views.server_management,name='server_management'),
    path('qa_testing/',views.qa_testing,name='qa_testing'),

    path('portfolio/',views.portfolio,name='portfolio'),

    path('contact/',views.contact,name='contact'),

    path('software_development/',views.software_development,name='software_development'),

    path('web_development/',views.web_development,name='web_development'),
    path('app_development/',views.app_development,name='app_development'),
    path('ai_and_ml/',views.ai_and_ml,name='ai_and_ml'),

    path('message/',views.message,name='message'),

    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminindex/',views.adminindex,name='adminindex'),
    path('add_job/',views.add_job,name='add_job'),
    path('view_job/',views.view_job,name='view_job'),
    path('delete_job/<int:job_id>/',views.delete_job,name='delete_job'),
    path('edit_job/<int:job_id>/',views.edit_job,name='edit_job'),

    path('apply/',views.apply,name='apply'),
    path('applications/',views.applications,name='applications'),
    path('delete_application/<int:application_id>/',views.delete_application,name='delete_application'),
    path('logout/',views.logout,name='logout'),

]
