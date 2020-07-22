from django.shortcuts import render

def home(request):
	return render(request, 'blog/home.html')


def english(request):
	return render(request, 'blog/english.html')

def math(request):
	return render(request, 'blog/math.html')

def science(request):
	return render(request, 'blog/science.html')

def login(request):
	return render(request, 'blog/login.html')
	
def register(request):
	return render(request, 'blog/register.html')

def about(request):
	return render(request, 'blog/about.html')




