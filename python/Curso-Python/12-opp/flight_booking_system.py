"""
Create two classes: Passenger and Flight. The Passenger class should store details such as name and passport_number. 
The Flight class should contain information like flight_number, origin, destination, and a list of passengers (which are instances of the Passenger class).

Additionally, implement an external function book_flight(flight, passenger) (not part of any of the previous classes) 
that adds a passenger to a flight. This function should ensure that a passenger cannot be 
booked more than once, which is determined by checking their passport_number.



Crea dos clases: Passengery Flight. La Passengerclase debe almacenar detalles como namey passport_number. 
La Flightclase debe contener información como flight_number, origin, destination, y una lista de passengers(que son instancias de la Passengerclase).

Además, implemente una función externa book_flight(flight, passenger) (que no forme parte de ninguna de las clases anteriores) 
que agregue un pasajero a un vuelo. Esta función debe garantizar que un pasajero no pueda ser reservado más de una vez, lo cual se determina comprobando su passport_number.

"""


# Your code goes here

#--------------------
# Passanger
#--------------------
class Passenger:

    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number


    def __repr__(self):
        return f"{self.name}, {self.passport_number}"



#--------------------
# Flight
#--------------------
class Flight:

    def __init__(self, flight_number, origin, destination, passengers = []):
        self.flight_number = flight_number 
        self.origin = origin 
        self.destination = destination
        self.passengers = passengers


    def __repr__(self):
        return f"{self.flight_number}, {self.origin}, {self.destination}, {self.passengers}"







def book_flight(flight, passanger):
    
    filtered = list(
        filter( lambda p: p.passport_number == passanger.passport_number, flight.passengers)
    )

    if len(filtered) == 0:
        flight.passengers.append(passanger)
    else:
        print(f"Passenger {passanger.name} already booked")


#--------------------
# Example usage
#--------------------

# Create passengers and flights
john = Passenger("John Doe", "P12345")
jane = Passenger("Jane Smith", "P67890")
flight1 = Flight("FL001", "NYC", "LA")



# Book flights
book_flight(flight1, john)
book_flight(flight1, jane)
book_flight(flight1, john)  # Should print "Passenger already booked!"



# Display flight details
print(f"Flight {flight1.flight_number} from {flight1.origin} to {flight1.destination}")
print("Has the following passengers:")
for passenger in flight1.passengers:
    print(passenger.name)