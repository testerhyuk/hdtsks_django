from django.shortcuts import render
from articleapp.models import CompanyRate

# Create your views here.
# def table_list(request):
#     company_list = CompanyRate.objects.all()
#     context = {"company_list": company_list}
#     return render(request, 'articleapp/table_list.html', context)

def table_list(request):
    start = request.POST['trip-start']
    end = request.POST['trip-end']
    company_list = CompanyRate.objects.filter(date__range=[start, end])
    company_list = company_list.order_by('date')
    context = {"company_list": company_list}
    return render(request, 'articleapp/table_list.html', context)

def select_date(request):
    return render(request, 'select_date.html')