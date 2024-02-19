from django.template import loader
from django.http import HttpResponse
from .models import Member
from django.template import RequestContext


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    # context_1 = RequestContext(request)
    # print(context_1)
    print(request)
    num1 = request.GET['num1']
    num2 = request.GET['num2']
    print(num1, num2)
    res = int(num1) + int(num2)
    context = {
        'product': {
            'num1': num1,
            'num2': num2,
            'result': res
        }
    }
    template = loader.get_template('result.html')
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id = id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers = Member.objects.all().values()
    # mymembers = Member.objects.values_list('firstname')
    # mymembers = Member.objects.filter(firstname='Puspendu', id=2).values()
    # equivalent to SELECT * FROM members_member WHERE firstname = 'Puspendu' AND ID = 2
    # mymembers = Member.objects.filter(firstname__startswith='S').values()
    # equivalent to SELECT * FROM members_member WHERE firstname LIKE 'S%'

    # print(mymembers)
    template = loader.get_template('template.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

