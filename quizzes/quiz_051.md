# Quiz051


# 1. UML Diagram

![CommSci 47](https://github.com/Rokyyz/UNIT4/assets/134658259/2a992d1f-19bf-44df-b0b9-4cbcfc3c7da4)


# 2. solutions


```.py
class Aircraft:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

    def get_info(self):
        return f"{self.model} (Capacity: {self.capacity})"

class Flight(Aircraft):
    def __init__(self, model, capacity, flight_number, origin, destination, departure_time):
        super().__init__(model, capacity)
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time

    def get_info(self):
        aircraft_info = super().get_info()
        return f"Flight {self.flight_number} from {self.origin} to {self.destination} departs at {self.departure_time}. Aircraft: {aircraft_info}"

def print_object_info(obj):
    print(obj.get_info())

aircraft = Aircraft("Boeing 737", 150)

flight = Flight("Boeing 737", 150, "AA123", "New York", "Los Angeles", "10:00 AM")

print("Aircraft Info:")
print_object_info(aircraft)
print("\nFlight Info:")
print_object_info(flight)

```

# 3. proof of work
<img width="1440" alt="Screenshot 2024-04-01 at 13 35 40" src="https://github.com/Rokyyz/UNIT4/assets/134658259/1faa86f8-c74f-4bf5-b337-dc93bfb9e915">

