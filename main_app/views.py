from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Car, Paint
from .forms import FuelingForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  fueling_form = FuelingForm()
  return render(request, 'cars/detail.html', { 'car': car, 'fueling_form': fueling_form })

class CarCreate(CreateView):
  model = Car
  fields = '__all__'
  success_url = '/cars/'

class CarUpdate(UpdateView):
  model = Car
  fields = '__all__'

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

def add_fueling(request, car_id):
  form = FuelingForm(request.POST)
  if form.is_valid():
    new_fuel = form.save(commit=False)
    new_fuel.car_id = car_id
    new_fuel.save()
  return redirect('detail', car_id=car_id)

def assoc_paint(request, car_id, paint_id):
  Car.objects.get(id=car_id).paint.add(paint_id)
  return redirect('detail', car_id=car_id)

def unassoc_paint(request, car_id, paint_id):
  Car.objects.get(id=car_id).paint.remove(paint_id)
  return redirect('detail', car_id=car_id)

class PaintList(ListView):
  model = Paint

class PaintDetail(DetailView):
  model = Paint

class PaintCreate(CreateView):
  model = Paint
  fields = '__all__'

class PaintUpdate(UpdateView):
  model = Paint
  fields = ['color', 'finish']

class PaintDelete(DeleteView):
  model = Paint
  success_url = '/paint/'