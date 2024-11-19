
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product

class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    login_url = reverse_lazy("users:login")

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    # fields = ('title', 'description', 'price', 'image', 'category')
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    login_url = reverse_lazy("users:login")

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.view_counter += 1
    #     self.object.save()
    #     return self.object


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ("title", "description", "price", "image", "category")
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:product_list')
    login_url = reverse_lazy("users:login")

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})
