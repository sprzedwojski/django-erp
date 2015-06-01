# from django.http import HttpResponse
from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import render, get_object_or_404
# from django.template import loader, RequestContext
from django.views import generic
from sales.models import Product, Client

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    # client_add_url=reverse_lazy('admin:sales_client_add')
    # product_add_url=reverse_lazy('admin:sales_product_add')
    # context = {'client_add_url': client_add_url,
    #            'product_add_url': product_add_url}
    # , context
    return render(request, 'sales/index.html')


@login_required
def products(request):
    # return HttpResponse("Hello world, welcome to Sales!")
    # latest_products_list = Product.objects.order_by('-delivery_date')[:5]
    # template = loader.get_template('sales/index.html');
    # context = RequestContext(request, {
    #     'latest_products_list': latest_products_list
    # })
    # output = ', '.join([p.product_name for p in latest_products_list])
    # return HttpResponse(template.render(context))
    latest_products_list = Product.objects.order_by('-delivery_date')
    context = {'latest_products_list': latest_products_list}
    return render(request, 'sales/products_list.html', context)


@login_required
def detail(request, product_id):
    # try:
    #     product = Product.objects.get(pk=product_id)
    # except Product.DoesNotExist:
    #     raise Http404("Product does not exist")
    # return render(request, 'sales/product_detail.html', {'product': product})
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'sales/product_detail.html', {'product': product})


@login_required
def clients(request):
    clients_list = Client.objects.order_by('client_name')
    context = {'clients_list': clients_list}
    return render(request, 'sales/clients_list.html', context)


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'sales/logout_success.html')


# class IndexView(generic.ListView):
#     template_name = 'sales/index.html'
#     context_object_name = 'latest_products_list'
#
#     def get_queryset(self):
#         return Product.objects.order_by('-delivery_date')[:5]


# class DetailView(generic.DetailView):
#     model = Product
    # template_name = 'sales/product_detail.html'