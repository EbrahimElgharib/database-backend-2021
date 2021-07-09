from django.shortcuts import render

# Create your views here.



from . forms import ReporterForm, AccidentForm
from .models import Accident, Reporter, Hospital
import math

#from geopy.geocoders import Nominatim



# Create your views here.



def accident_report(request):
    if request.method=='POST':

        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()







        form1 = AccidentForm(request.POST)
        if form1.is_valid():
            lat = form1.cleaned_data.get('place_lat')
            Long = form1.cleaned_data.get('place_long')
            print(lat, Long)
            coord1 = (lat, Long)   # of accident
            hos = Hospital.objects.values('place_lat','place_long')  # object contains two columns as dictionary
            hos_id = Hospital.objects.values('hospital_id')  # list of dictionaries
            print(hos_id)
            
            #print(hos_id.)

            total_distance = []

            for i in (hos):
                print(i)
                coord2 = (i['place_lat'], i['place_long'])  # as it is a dictionary
                print(coord2)
                d = haversine(coord1, coord2)
                total_distance.append(d) 
                print(d)
            print(total_distance)
            mini_d = min(total_distance)
            print(mini_d)
            y = total_distance.index(mini_d)  
            print(y)  

            keylist = ['hospital_id']
            listOfLIsts = bycol_decl(hos_id, keylist)
            print(listOfLIsts)
            desired_id = listOfLIsts[0][y]
            print(desired_id)

            
            
            




            #form1.save()

    
            

    else:
        form = ReporterForm()
        form1 = AccidentForm()
    context = {
        'form': form,
        'form1': form1

    }

    return render(request, 'ambulance/ReporterData_F.html',context)
    


    

def haversine(coord1, coord2):
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)
    
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))


            #instance = form.save(commit = False)
            #instace.accident = request.Accident
            #instace.save()

            #lat = form1.place_lat
            #Long = form1.place_long


def bycol_decl(lod, keylist):
    return  [[row[key] for row in lod] for key in keylist]
