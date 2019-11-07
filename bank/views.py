from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Table
# from .forms import TableForm
from django.views.generic.list import ListView
# Create your views here.

#
# def home(request):
#     context = {'text': 'Выполнение тестового задания для Росбанка'}
#     print(context)
#     return render(request, 'main.html', context)

# class TestView(ListView):
#     model = Table
#     template_name = 'main.html'
#     context_object_name = 'banks'


def home_form(request):
    obj = Table.objects.get(id=1)
    context = {
        # 'month': obj.month,
        # 'TO': obj.to,
        # 'City': obj.city,
        # 'Office': obj.office,
        # 'Group of indicators': obj.financial_group,
        # 'Indicator': obj.financial
        # 'Value': obj.value
        'object': obj
    }
    return render(request, 'main.html', context)


    # def table_form(request):
    #     obj = Table.objects.get(id=2)
    #     context = {
    #         # 'month': obj.month,
    #         # 'TO': obj.to,
    #         # 'City': obj.city,
    #         # 'Office': obj.office,
    #         # 'Group of indicators': obj.financial_group,
    #         # 'Indicator': obj.financial
    #         # 'Value': obj.value
    #         'object': obj
    #     }
    #     return render(request, 'main.html', context)


    # table = TestTableTables(TestTable.objects.all())
# def home(request):
#         if request.method == 'GET':
#                 return HttpResponse('Запрос получен')
#         elif request.method == 'POST':
#                 return  HttpResponse('Запрос опубликован')


