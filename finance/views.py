import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from hr.models import SalaryHistory
from sales.models import Product


logger = logging.getLogger('django.request')


@login_required
def index(request):
    return render(request, 'finance/index.html')


@login_required
def results(request):
    products_list = Product.objects.order_by('delivery_date')
    salaries_list = SalaryHistory.objects.order_by('shi_month')
    context = {'products_list': products_list, 'salaries_list': salaries_list}
    # months = []
    # cur_month = []
    # for product in products_list:
    #     date = product.delivery_date
    #
    #     logger.debug(date.year)
    return render(request, 'finance/results.html', context)
