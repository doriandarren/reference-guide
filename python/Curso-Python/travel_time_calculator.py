
#vehicle_type = input("Choose a mode of transport [car, train, plane]: ").lower()

vehicle_type = 'plane'

DISTANCE_KM = 482.8

if vehicle_type != 'car' and vehicle_type != 'train' and vehicle_type != 'plane':
    print("Invalid mode of transport.")
else:
    if vehicle_type == 'car':
        hours = (DISTANCE_KM / 96.6) + 1
    
    elif vehicle_type == 'train':
        hours = (DISTANCE_KM / 48.3) + 1
    
    else:
        hours = (DISTANCE_KM / 804.7) + 2
        
    print(f"Total time: {hours:.2f} hours")
    
    

