class Flight:
    def __init__(self, flight_num, depatrue_time, arrival_time):
        self.__flight_num = flight_num
        self.__departure_time = depatrue_time
        self.__arrival_time = arrival_time

    @property
    def flight_num(self):
        return self.__flight_num
    @property
    def departure_time(self):
        return self.__departure_time
    @property
    def arrival_time(self):
        return self.__arrival_time
    
    @departure_time.setter
    def departure_time(self, value):
        self.__departure_time = value

    @arrival_time.setter
    def arrival_time(self, value):
        self.__arrival_time = value

    def get_flight_time(self):

        flight_time_hours = self.arrival_time[3] - self.departure_time[3]
        flight_time_minutes = self.arrival_time[4] - self.departure_time[4]
        flight_time_sec = self.arrival_time[5] - self.departure_time[5]

        flight_time_minutes += flight_time_hours * 60 + flight_time_sec / 60

        return int(flight_time_minutes)

class Itineray():
    def __init__(self, flights):
        self.flights = flights
    
    def get_total_travel_time(self):
        
        start_hour = self.flights[0].departure_time[3]
        start_min = self.flights[0].departure_time[4]

        end_hour = self.flights[-1].arrival_time[3]
        end_min = self.flights[-1].arrival_time[4]

        total_travel_time = (end_hour - start_hour) * 60 + (end_min - start_min)

        return total_travel_time

    def get_total_flight_time(self):
        lis_of_minutes_in_air = []
        index = 0

        for i in range(0, len(self.flights)):
            lis_of_minutes_in_air.append(Flight.get_flight_time(self.flights[index]))
            index +=1

        return sum(lis_of_minutes_in_air)


def main():
    flights = []

    flights.append(Flight("US230", (2014, 4, 5, 5, 5, 0), (2014, 4, 5, 6, 15, 0)))
    flights.append(Flight("US235", (2014, 4, 5, 6, 55, 0), (2014, 4, 5, 7, 45, 0)))
    flights.append(Flight("US237", (2014, 4, 5, 9, 35, 0), (2014, 4, 5, 12, 55, 0)))

    itinerary = Itineray(flights)

    print(itinerary.get_total_travel_time())

    print(itinerary.get_total_flight_time())
   

if __name__ == "__main__":
    main()
