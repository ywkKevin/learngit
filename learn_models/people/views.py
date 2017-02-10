from django.shortcuts import render, render_to_response
from django.template import loader, Context, RequestContext  
from django.http import HttpResponse, HttpResponseRedirect    
from people.models import Student
# from django.core import serializers
# import json

# Create your views here.
def login(request):
	if request.POST.has_key('info'):
		info = request.POST['info']
		if request.POST.has_key('password'):
			password = request.POST['password']
		if request.POST.has_key('id'):
			aid = request.POST['id']
		student = Student.objects.get(id = aid)
		student.password = password
		student.save()
		return render(request, 'login.html', {'info':info})
	else:
		return render(request, 'login.html')

def checkLogin(request):
	if request.POST.has_key('name'):
		name = request.POST['name']
	if request.POST.has_key('password'):
		password = request.POST['password']
	student = Student.objects.filter(name = name, password = password)
	if student:
		student = Student.objects.get(name = name)
		# student = serializers.serialize("json", student)
		# student = json.loads(student)
		# student = Student.objects.get(name = name, password = password)
		# student.toJSON()
		# return HttpResponse(student[0]['fields']['name'])
		# [{"model": "people.student", "pk": 2, "fields": {"name": "zhao yun", "age": 19, "password": "zxc", "sex": "F"}}]
		request.session['student'] = student
		return HttpResponseRedirect('/index/')
	else:
		error = "The account password is incorrect or the account does not exist, please go to register"
		return render(request, 'login.html', {'error':error})

def register(request):
	return render(request, 'register.html')

def registerUI(request):
	if request.POST.has_key('name'):
		name = request.POST['name']
	if request.POST.has_key('age'):
		age = request.POST['age']
	if request.POST.has_key('sex'):
		sex = request.POST['sex']
	if request.POST.has_key('password'):
		password = request.POST['password']
	if request.POST.has_key('cp'):
		cp = request.POST['cp']
	# if name == '' | age == '' | sex == '' | password == '' | cp == '':
	# 	error = "Your information is incomplete, please complete"
	# 	return render(request, 'register.html', {'error':error})
	student = Student.objects.filter(name = name)
	if student:
		error = "The account is exist, please input again"
		return render(request, 'register.html', {'error':error})
	else:
		if password != cp:
			error = "Passwords do not match. Please re-enter"
			return render(request, 'register.html', {'error':error})
		student = Student()
		student.name = name
		student.age = age
		student.sex = sex
		student.password = password
		student.save()
		request.session['student'] = student
		return render(request, 'register_success.html', {'student':student})

def index(request):
	student = request.session.get('student')
	return render(request, 'index.html', {'student':student})

def login_Out(request):
	del request.session['student']
	return HttpResponseRedirect('/login/')

def student_List(request):
	studentList = Student.objects.all()
	return render(request, 'student_List.html', {'studentList':studentList})

def show_Password(request, aid):
	student = Student.objects.get(id = aid)
	return render(request, 'updata_Password.html', {'student':student})

def delete(request, aid):
	student = Student.objects.get(id = aid)
	student.delete()
	return HttpResponseRedirect('/student_List/')

def detail(request, aid):
	student = Student.objects.get(id = aid)
	return render(request, 'detail.html', {'student':student})

def detailUI(request, aid):
	student = Student.objects.get(id = aid)
	if student:
		if request.POST.has_key('name'):
			name = request.POST['name']
		if request.POST.has_key('age'):
			age = request.POST['age']
		if request.POST.has_key('sex'):
			sex = request.POST['sex']
		student.name = name
		student.age = age
		student.sex = sex
		student.save()
		return HttpResponseRedirect('/student_List/')