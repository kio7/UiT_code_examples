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

    def get_flight_time(self, departure_time, arrival_time):
        flight_time_hours = arrival_time[3] - departure_time[3]
        flight_time_minutes = arrival_time[4] - departure_time[4]

        flight_time_minutes += flight_time_hours * 60

        return flight_time_minutes


class Itineray():
    def __init__(self, flights):
        self.flights = flights
    
    def get_total_travel_time(self):
        start_hour = self.flights[0][1][3]
        start_min = self.flights[0][1][4]

        end_hour = self.flights[-1][2][3]
        end_min = self.flights[-1][2][4]

        total_travel_time = (end_hour - start_hour) * 60 + (end_min - start_min)

        return total_travel_time

    def get_total_flight_time(self):
        lis_of_minutes_in_air = []
        index = 0

        for i in range(0, len(self.flights)):
            start_hour = self.flights[index][1][3]
            start_min = self.flights[index][1][4]

            end_hour = self.flights[index][2][3]
            end_min = self.flights[index][2][4]

            temp = (end_hour - start_hour) * 60 + (end_min - start_min)

            lis_of_minutes_in_air.append(temp)
            index +=1

        return sum(lis_of_minutes_in_air)


def main():
    flights = []

    flights.append(["US230", (2014, 4, 5, 5, 5, 0), (2014, 4, 5, 6, 15, 0)])
    flights.append(["US235", (2014, 4, 5, 6, 55, 0), (2014, 4, 5, 7, 45, 0)])
    flights.append(["US237", (2014, 4, 5, 9, 35, 0), (2014, 4, 5, 12, 55, 0)])

    flight_US230 = Flight(flights[0][0], flights[0][1], flights[0][2])
    flight_US235 = Flight(flights[1][0], flights[1][1], flights[1][2])
    flight_US237 = Flight(flights[2][0], flights[2][1], flights[2][2])

    itinerary = Itineray(flights)
    
    print(itinerary.get_total_travel_time())

    print(itinerary.get_total_flight_time())


if __name__ == "__main__":
    main()
