from django.shortcuts import render
from django.http import HttpResponseRedirect
#  models 
from hotellist.models import Hotellist
from mainapp.models import Login


# Create your views here.

def hotellist(request, hotelstate, id):
    if (
        'user_{}_uname'.format(id) not in request.session
        and 'user_{}_upass'.format(id) not in request.session
        and 'user_{}_uemail'.format(id) not in request.session
    ):
        return HttpResponseRedirect('/login/')

    elif (
        'user_{}_uname'.format(id) in request.session
        and 'user_{}_upass'.format(id) in request.session
        and 'user_{}_uemail'.format(id) in request.session
    ):
        user = Login.objects.get(
            username=request.session.get('user_{}_uname'.format(id)),
            email=request.session.get('user_{}_uemail'.format(id)),
            password=request.session.get('user_{}_upass'.format(id)),
        )
        username = user.username
        password = user.password
        if Login.objects.filter(username=username, password=password).exists():
            if hotelstate == 'all':
                data = Hotellist.objects.all().order_by('?')
            elif hotelstate == 'others':
                data = (Hotellist.objects.filter(state='sidama' ) | Hotellist.objects.filter(state='somali')).order_by('?')
            else:
                data = Hotellist.objects.filter(state=hotelstate).order_by('?')
            url = '/dashboard/{}'.format(id)
            # this is for showing the user name in place of dashboard button after login ....
            dash_board_name = username[0:7]
            datamain = {
                'un': username,
                'pw': password,
                'url': url,
                'data': data,
                'id': id,
                'dn': dash_board_name,
                'hstate': hotelstate,
            }
            return render(request, 'hotellist.html', datamain)
        return render(request, 'hotellist.html', datamain)
