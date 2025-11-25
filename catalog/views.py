from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Product, Category
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if product.is_published:
            if not request.user.has_perm('catalog.can_unpublish_product'):
                raise PermissionDenied('Нет прав на снятие с публикации')
            product.is_published = False

            product.save()

        return redirect('catalog:product_details', pk=pk)


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

    def get_form_class(self):
        user = self.request.user

        if user == self.object.owner:
            return ProductForm
        else:
            raise PermissionDenied('Нет доступа редактировать продукт')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    extra_context = {'categories': Category.objects.all()}
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:home')

    def get_form_class(self):
        user = self.request.user

        if user == self.object.owner or user.has_perm('catalog.delete_product'):
            return ProductForm
        else:
            raise PermissionDenied('Нет доступа удалять продукт')


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

