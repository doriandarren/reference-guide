# Your code goes here


# Example usage

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