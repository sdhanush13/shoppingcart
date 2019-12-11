from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from cashReg.forms import SignUpForm, AddProductForm
from django.views import generic
from django.views.generic import DetailView
from cashReg.models import Cart
from cashReg.models import AddProduct
from django.urls import reverse, reverse_lazy


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            User = authenticate(username=username, password=raw_password)
            login(request, User)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def AddProductView(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddProductForm()
    return render(request, 'addproduct.html', {'form': form})


class ProductListView(generic.ListView):
    model = AddProduct
    context_object_name = 'prod_list'
    template_name = 'product.html'

    def get_queryset(self):
        return AddProduct.objects.order_by('Product_Name')


def Cartview(request):
    cart = Cart.objects.all()[0]
    context = {"cart": cart}
    template = "cartview.html"
    return render(request, template, context)


def update_cart(request, pk):
    cart = Cart.objects.all()[0]
    try:
        book = AddProduct.objects.get(pk=pk)
    except ObjectDoesNotExist:
        pass
    if book not in cart.products.all():
        cart.products.add(book)
    else:
        cart.products.remove(book)
    new_total = 0.00
    for item in cart.products.all():
        new_total += item.Price
    cart.total = new_total
    cart.save()
    return HttpResponseRedirect(reverse_lazy('cart'))


def ThankYou(request):
    return render(request, "thankyou.html", context=None)
