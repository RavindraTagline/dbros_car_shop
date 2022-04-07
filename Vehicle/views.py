from django.core.mail import EmailMultiAlternatives
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views import View

from .filters import CarFilters
from .forms import BuyerForm, CarForm
from .models import Buyer, Car


def CarAdd(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Thank You')
    else:
        form = CarForm()
    return render(request, 'main/car_add.html', {'form': form})


def CarUpdate(request):
    return render(request, 'main/update_car.html')


def ThankYou(request):
    return render(request, 'main/thanks_page.html')


def HomePage(request):
    if request.method == 'GET':

        all = Car.objects.all().order_by('-id')
        myFilter = CarFilters(request.GET, queryset=all)
        all = myFilter.qs

        # car_list = Car.objects.all().order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(all, 10)

        if all.exists():
            try:
                cars = paginator.page(page)
            except PageNotAnInteger:
                cars = paginator.page(1)
            except EmptyPage:
                cars = paginator.page(paginator.num_pages)
            return render(
                request, 'main/homepage.html', {'data': cars, 'myFilter': myFilter})
        else:
            return render(
                request, 'main/homepage.html', {'error': 'No results found for your filter'})


def ChangeStatus(request, pk):
    buy_car = Car.objects.get(pk=pk)
    buy_car.available = 'Available'
    buy_car.save()
    return redirect('Home Page')


class BuyerCarView(View):
    def get(self, request, **kwrgs,):
        buy_car = Car.objects.get(id=kwrgs['pk'])
        form_data = BuyerForm
        return render(request, 'main/buy_car.html', {'form_data': form_data, 'buy_car': buy_car})

    def post(self, request, **kwrgs):
        buy_car = Car.objects.get(id=kwrgs['pk'])
        form_data = BuyerForm(request.POST)
        seller_commission = (buy_car.price * 5/100)
        net_amount = (buy_car.price - seller_commission)
        if form_data.is_valid():
            name = form_data.cleaned_data['name']
            mobile = form_data.cleaned_data['mobile']
            buyer_data = Buyer(
                car=buy_car, buyer_name=name, mobile=mobile)
            buyer_data.save()
            buy_car.available = 'Sold'
            buy_car.save()
            bd = {
                'name': name, 'mobile': mobile, 'commission': seller_commission, 'car_model': buy_car.car_model,
                'brand': buy_car.make, 'year': buy_car.year, 'price': buy_car.price,
                'net_amount': net_amount}
            html_template = render_to_string(
                'main/email_data.html', {'bd': bd})
            subject = 'Django Mail',
            from_mail = 'ravindra.tagline@gmail.com'
            to_mail = 'ravindra.tagline@gmail.com'
            message = EmailMultiAlternatives(
                subject, html_template, from_mail, [to_mail])
            message.content_subtype = 'html'
            message.send()

            return redirect('Thank You')
        else:
            return render(request, 'main/buy_car.html', {'form_data': form_data})
