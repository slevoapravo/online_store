from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Product, Category
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    model = Product
    context_object_name = 'prods'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    extra_context = {'categories': Category.objects.all()}
    success_url = reverse_lazy('catalog:home')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    extra_context = {'categories': Category.objects.all()}
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:home')


class ContactView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'Спасибо {name}, с номером "{phone}" и сообщением "{message}". Данные в сохранность!')

        return HttpResponseRedirect(reverse_lazy('catalog:home'))
