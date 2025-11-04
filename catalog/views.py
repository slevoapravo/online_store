from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Product, Category
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import ProductForm


class ProductListView(ListView):
    """
    Отображение списка продуктов.
    """
    model = Product
    context_object_name = 'prods'


class ProductDetailView(DetailView):
    """
    Отображение детали продукта.
    """
    model = Product
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    """
    Обновление информации о продукте.
    """
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    extra_context = {'categories': Category.objects.all()}
    success_url = reverse_lazy('catalog:home')


class ProductCreateView(CreateView):
    """
    Создание нового продукта.
    """
    model = Product
    form_class = ProductForm
    extra_context = {'categories': Category.objects.all()}
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    """
    Удаление продукта.
    """
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:home')


class ContactView(View):
    """
    Контактная форма для отправки сообщений.
    """
    template_name = 'catalog/contacts.html'

    def get(self, request):
        """
        Обработка GET-запроса для отображения контактной формы.
        """
        return render(request, self.template_name)

    def post(self, request):
        """
        Обработка POST-запроса для отправки сообщения.
        """
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Логирование полученных данных
        print(f'Спасибо {name}, с номером "{phone}" и сообщением "{message}". Данные в сохранность!')

        return HttpResponseRedirect(reverse_lazy('catalog:home'))
