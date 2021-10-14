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


    def get_flight_time(self, departure_time: departure_time, arrival_time: arrival_time):
        flight_time_hours = arrival_time[3] - departure_time[3]
        flight_time_minutes = arrival_time[4] - departure_time[4]

        flight_time_minutes += flight_time_hours * 60
        return flight_time_minutes


class Itineray:
    pass


def main():
    
    flights = []

    flights.append(Flight("US230", (2014, 4, 5, 5, 5, 0), (2014, 4, 5, 6, 15, 0)))

    flights.append(Flight("US235", (2014, 4, 5, 6, 55, 0), (2014, 4, 5, 7, 45, 0)))

    flights.append(Flight("US237", (2014, 4, 5, 9, 35, 0), (2014, 4, 5, 12, 55, 0)))



    test = Flight.get_flight_time("US230", (2014, 4, 5, 5, 5, 0), (2014, 4, 5, 6, 15, 0))
    print(test)

#    itinerary = Itinerary(flights)

#    print(itinerary.getTotalTravelTime())

#    print(itinerary.getTotalFlightTime())


if __name__ == "__main__":
    main()