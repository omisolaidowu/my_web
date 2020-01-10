from django.shortcuts import render
from .models import Register
from .forms import register

# Create your views here.
def home(request):
	a=('very good')
	b=('not so good')
	context={'a':a, 'b':b}


	return render(request, 'home.html', context)


def registration(request):
	form    = register()
	if request.method=="POST":
		form    = register(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			Register.objects.create(**form.cleaned_data)
		else:
			print(form.errors)
	context ={"form": form}

	return render(request, 'register.html', context)

	
	

