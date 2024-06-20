from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def price(request):
    return HttpResponse('this is price page')


def homepage(request, id=None):
    if id == None:
        return render(request, 'index.html')
    else:
        if (
            'user_{}_uname'.format(id) in request.session
            and 'user_{}_uemail'.format(id) in request.session
            and 'user_{}_upass'.format(id) in request.session
        ):
            url = '/dashboard/{}'.format(id)
            data = {'id': id, 'url': url}
            return render(request, 'index2.html', data)
        else:
            return HttpResponseRedirect('/')



def about(request, id=None):
    if id == None:
        return render(request, 'about.html')
    else:
        if (
            'user_{}_uname'.format(id) in request.session
            and 'user_{}_uemail'.format(id) in request.session
            and 'user_{}_upass'.format(id) in request.session
        ):
            url = '/dashboard/{}'.format(id)
            data = {'id': id, 'url': url}
            return render(request, 'about2.html', data)
        else:
            return HttpResponseRedirect('/about/')



def services(request, id=None):
    if id == None:
        return render(request, 'services.html')
    else:
        if (
            'user_{}_uname'.format(id) in request.session
            and 'user_{}_uemail'.format(id) in request.session
            and 'user_{}_upass'.format(id) in request.session
        ):
            url = '/dashboard/{}'.format(id)
            data = {'id': id, 'url': url}
            return render(request, 'services2.html', data)
        else:
            return HttpResponseRedirect('/services/')

