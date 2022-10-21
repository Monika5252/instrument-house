from django.shortcuts import render
from django.views.generic import View, TemplateView




class HomeView(View):
    template_name = "home.html"
    def get(self, request):        
        labels = []
        data = []
        from imd.imdapp.models import Stock
        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
        from imd.imdapp.models import SaleBill
        sales = SaleBill.objects.order_by('-time')[:3]
        from imd.imdapp.models import PurchaseBill
        purchases = PurchaseBill.objects.order_by('-time')[:3]
        context = {
            'labels'    : labels,
            'data'      : data,
            'sales'     : sales,
            'purchases' : purchases
        }
        return render(request, self.template_name, context)

class AboutView(TemplateView):
    template_name = "about.html"


