from django.shortcuts import render,redirect
from home.models import AddMovie
# Create your views here.
def log_in(request):
    if 'username' in request.session:
        return redirect(Home_page)
    if request.POST:
        logi = request.POST
        if logi["username"] == 'rabeeh'and logi["password"] == '1234':
            request.session['username'] = logi["username"]
            return redirect(Home_page)
        else:
            error_message = 'Incorrect username or password'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request,'login.html')

def Home_page(request):
    std_dtl = {
        'malayalam': AddMovie.objects.all(),
    }
    if 'username'in request.session:
        res = render(request,'home.html',std_dtl)
        res['Cache-Control'] = 'no-store, must-revalidate'
        res['Pragma'] = 'no-cache'
        res['Expires'] = '0'
        return res
    return redirect(log_in)

def log_out(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(log_in)

    






# 'malayalam':[{
#                     "title":'CHAVER',
#                     "date":2023,
#                     'img':'https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC/et00362719-qdurzsjcxn-portrait.jpg',
#                 },{
#                     "title":'Paapachan Olivilaan',
#                     "date":2023,
#                     'img':'https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC/et00363949-etyqulygek-portrait.jpg'

#                 },{
#                     "title":'kamala',
#                     "date":2019,
#                     'img':'https://static.toiimg.com/thumb/msid-71836903,width-400,resizemode-4/71836903.jpg'
#                 },{
#                     "title":'Neymar',
#                     "date":2023,
#                     'img':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtep1Gbcpr6dXYKscnngIuQueU-LTyTM-5gg&usqp=CAU'
#                 },{
#                     "title":'King of Kotha',
#                     "date":2023,
#                     'img':'https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC/et00351659-shdgarxkrg-portrait.jpg'
#                 },{
#                     "title":'Vathil',
#                     "date":2023,
#                     'img':'https://assets-in.bmscdn.com/discovery-catalog/events/tr:w-400,h-600,bg-CCCCCC/et00368432-eavtudexka-portrait.jpg'
#                 },{
#                     "title":'Drishiyam',
#                     "date":2015,
#                     'img':'https://nettv4u.com/fileman/Uploads/redefined-the-Malayalam-film-industry/image011.jpg'
#                 },{
#                     "title":'Vishudhen Mojo',
#                     "date":2015,
#                     'img':'https://totalkerala.com/wp-content/uploads/2022/08/17-3.jpg'
#                 },{
#                     "title":'Master',
#                     "date":2015,
#                     'img':'https://static.toiimg.com/thumb/msid-101172246,width-1280,resizemode-4/101172246.jpg'
#                 },{
#                     "title":'Bangloor Days',
#                     "date":2015,
#                     'img':'https://img1.hotstarext.com/image/upload/f_auto,t_vl/sources/r1/cms/prod/5071/635071-v'
#                 }],