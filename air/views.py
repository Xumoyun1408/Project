from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Air, Reys, City
from .forms import AirForm, CityForm

# -------------------------------------------------------------------------------------------
def home(request):
    airs = Air.objects.all()
    categories = Category.objects.all()
    reys = Reys.objects.all()
    return render(request, 'home.html', context={"airs": airs, "cats": categories, "reys": reys})
# -------------------------------------------------------------------------------------------
def category(request, id):
    cat = get_object_or_404(Category, id=id)
    airs = cat.airs.all()
    reys = Reys.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', context={"city": city, "reys": reys,"airs": airs, "cats": categories})



def batafsil(request, id):
    air = get_object_or_404(Air, id=id)
    categories = Category.objects.all()
    reys = Reys.objects.all()
    return render(request, 'batafsil.html', context={'air': air, "cats": categories, "reys": reys})



def create_air(request):
    form = AirForm()
    if request.method == "POST":
        form = AirForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create_air.html', context={"form": form})



def update_air(request, id):
    air = get_object_or_404(Air, id=id)
    if request.method == "POST":
        form = AirForm(request.POST, request.FILES, instance=air)
        if form.is_valid():
            form.save()
            return redirect('batafsil', id=air.id)
    else:
        form = AirForm(instance=air)
    return render(request, 'create_air.html', context={"form": form})



def delete_air(request, id):
    air = get_object_or_404(Air, id=id)
    air.delete()
    return redirect('home')

# -------------------------------------------------------------------------------------------
def reys(request):
    reys = Reys.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', context={"reys": reys, "cats": categories})

def city(request, id):
    rey = get_object_or_404(Reys, id=id)
    city = rey.reys.all()
    reys = Reys.objects.all()
    categories = Category.objects.all()
    return render(request, 'reys.html', context={'city':city, "reys": reys, "cats": categories})


def more(request, id):
    city = get_object_or_404(City, id=id)
    reys = Reys.objects.all()
    categories = Category.objects.all()
    return render(request, 'more.html', context={"city": city, 'reys': reys, "cats": categories})



def create_city(request):
    form = CityForm()
    if request.method == "POST":
        form = CityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create_city.html', context={"form": form})



def update_city(request, id):
    city = get_object_or_404(City, id=id)
    if request.method == "POST":
        form = CityForm(request.POST, request.FILES, instance=city)
        if form.is_valid():
            form.save()
            return redirect('more', id=city.id)
    else:
        form = CityForm(instance=city)
    return render(request, 'create_city.html', context={"form": form})



def delete_city(request, id):
    city = get_object_or_404(City, id=id)
    city.delete()
    return redirect('home')