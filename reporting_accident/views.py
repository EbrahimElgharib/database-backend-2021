from django.db.models.aggregates import Min
from django.shortcuts import render

# Create your views here.



from . forms import ReporterForm, AccidentForm
from .models import Accident, Reporter, Hospital, Station, Crew
import math

#from geopy.geocoders import Nominatim



# Create your views here.



def accident_report(request):
    if request.method=='POST':

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
            print(desired_id)        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Nearst Hospital ID


            station_ambulance = Station.objects.values('place_lat','place_long')
            print(station_ambulance)
            station_ambulance_id = Station.objects.values('station_id')
            print(station_ambulance_id)
            total_stations_distances = []
            for s in station_ambulance:
                print(s)
                coord_station = (s['place_lat'], s['place_long'])  # as it is a dictionary
                print(coord_station)
                station_distance = haversine(coord1, coord_station)
                total_stations_distances.append(station_distance)
                print(station_distance)
            print(total_stations_distances)
            mini_distance = min(total_stations_distances)
            print(mini_distance)
            min_dis_index = total_stations_distances.index(mini_distance)  
            print(min_dis_index)  
            keylist2 = ['station_id']
            listOfLIsts2 = bycol_decl(station_ambulance_id, keylist2)
            print(listOfLIsts2)
            desired_station_id = listOfLIsts2[0][min_dis_index]
            print(desired_station_id)      #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Nearst Station ID


            # query to select crew according to the station
            crews = Crew.objects.filter(station = desired_station_id, crew_status = 'Available',  )
            print(crews)
            k = crews.aggregate(Min ('number_of_accidents'))
            j = k['number_of_accidents__min']
            print(j)
            
            #g = Crew.objects.filter(station = crews, number_of_accidents = k  )
            g = Crew.objects.filter(number_of_accidents = j , station=desired_station_id, crew_status='Available'  )
            
            a = g.values_list('pk')
            h = list(a)
            print(h)
            


            '''
            w = h[0]
            r = w[0]     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> crewID
            print(g, crews,list(a), w, r)
            
        
            Y = Crew.objects.get(crew_id =r )
            Y.crew_status = 'in duty'
            Y.save()
            print(Y)
            '''


            


            #form1.save()
            
            instance = form1.save(commit = False)
            instance.Hospital = desired_id
            instance.save()
            print("kkk")
           

            
            
            
        form = ReporterForm(request.POST)
        if form.is_valid():
            #z = Accident.objects.values('accident_id').filter(place_lat =lat )['accident_id']
            #print(z)
            form.save()
        
                
            #acc = Accident.objects.get(place_lat =lat )
            #acc_id = acc.accident_id
            #print(acc_id)




            #form.save()




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
