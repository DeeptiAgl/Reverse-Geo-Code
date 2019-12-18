import geocoder
import pandas as pd
CoStar = pd.read_csv(r"abc.csv",encoding = "ISO-8859-1",low_memory=False)
print("File Loaded into the system")
CoStar['LAT LON'] = CoStar["Latitude"].astype(str) +"," + CoStar["Longitude"].astype(str)
latlon = (CoStar['LAT LON'] ).tolist()
print(f"{CoStar['LAT LON']} lat: {CoStar.Latitude} lon: {CoStar.Longitude} ")
ZC = []
for address in latlon:
    g = geocoder.mapquest(address, method='reverse', key='****') #key=please create youw own key at mapquest website
    
    # g = geocoder.mapquest([34.036453, -118.226467], method='reverse', key='PGpRDQRBrH7DqjF0OkYODgc2lmODm2c9')
    
    if g :
        ZC.append(g.postal)
        print(g.postal)
        # longitude.append(location.lng)
    else:
        ZC.append(0)
CoStar['ZC'] = ZC
CoStar.to_csv('CoStar_ZC.csv')