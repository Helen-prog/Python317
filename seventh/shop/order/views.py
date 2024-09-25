from django.shortcuts import render
from django.views.generic import CreateView
from .forms import OrderForm
from django.urls import reverse_lazy
from .models import Order


class OrderCreateView(CreateView):
    form_class = OrderForm
    template_name = 'order/order-create.html'
    success_url = reverse_lazy('full-order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Store - Оформление заказа"
        return context

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)


def full_order(request):
    order = Order.objects.all().order_by("created").last()
    order.update_after_payment()
    return render(request, 'order/success.html')
