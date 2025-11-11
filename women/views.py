from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from women.models import Category, Human
from women.forms import FormHuman
from django.contrib.auth.mixins import LoginRequiredMixin

class BaseMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class HomeView(BaseMixin, ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'women/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_humans'] = Human.objects.all()[:6]
        return context

class CreateHuman(LoginRequiredMixin, BaseMixin, CreateView):
    model = Human
    form_class = FormHuman
    success_url = reverse_lazy('women:index')
    template_name = 'women/human_create.html'
    login_url = '/users/login/'
    def form_valid(self, form):
        if not form.instance.slug:
            from django.utils.text import slugify
            form.instance.slug = slugify(form.instance.name_h)
        return super().form_valid(form)

class UpdateHuman(BaseMixin, UpdateView):
    model = Human
    form_class = FormHuman
    template_name = 'women/human_create.html'
    success_url = reverse_lazy('women:index')

class AllHumansView(BaseMixin, ListView):
    model = Human
    template_name = 'women/all_humans.html'
    context_object_name = 'humans'
    paginate_by = 12

class CategoryDetailView(BaseMixin, DetailView):
    model = Category
    template_name = 'women/category_detail.html'
    context_object_name = 'category'
    slug_url_kwarg = 'cat_slug'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['humans'] = category.humans.all()
        return context

class HumanDetailView(BaseMixin, DetailView):
    model = Human
    template_name = 'women/human_detail.html'
    context_object_name = 'human'
    slug_url_kwarg = 'human_slug'
    slug_field = 'slug'


class AboutView(BaseMixin, TemplateView):
    template_name = 'women/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Реальная статистика из базы данных
        context['women_count'] = Human.objects.count()
        context['categories_count'] = Category.objects.count()
        return context