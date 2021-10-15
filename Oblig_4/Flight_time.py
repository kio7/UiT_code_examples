from datetime import datetime

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
        start_hour = self.departure_time.hour
        start_min = self.departure_time.minute
        start_sec = self.departure_time.second

        end_hour = self.arrival_time.hour
        end_min = self.arrival_time.minute
        end_sec = self.arrival_time.second

        total_flight_time = (end_hour - start_hour) * 60 + end_min - start_min + (end_sec - start_sec) / 60

        return int(total_flight_time)

class Itineray():
    def __init__(self, flights):
        self.flights = flights

    def get_total_travel_time(self): 
        latest_arrival_time = 0.0
        earliest_departure_time = 1440.1

        for i in range(0, len(self.flights)):
            temp = self.flights[i].departure_time
            start_hour = temp.hour
            start_min = temp.minute
            start_sec = temp.second

            departure_time = start_hour * 60 + start_min + start_sec / 60
            
            if departure_time < earliest_departure_time:
                earliest_departure_time = departure_time
        
        for i in range(0,len(self.flights)):
            temp = self.flights[i].arrival_time
            end_hour = temp.hour
            end_min = temp.minute
            end_sec = temp.second

            arrival_time = end_hour * 60 + end_min + end_sec / 60

            if arrival_time > latest_arrival_time:
                latest_arrival_time = arrival_time

        total_travel_time = latest_arrival_time - earliest_departure_time
        return int(total_travel_time)


    def get_total_flight_time(self):

        lis_of_minutes_in_air = [Flight.get_flight_time(self.flights[x]) for x in range(0, len(self.flights))]

        return sum(lis_of_minutes_in_air)


def main():
    flights = []

    flights.append(Flight("US230", datetime(2014, 4, 5, 5, 5, 0), datetime(2014, 4, 5, 6, 15, 0)))
    flights.append(Flight("US235", datetime(2014, 4, 5, 6, 55, 0), datetime(2014, 4, 5, 7, 45, 0)))
    flights.append(Flight("US237", datetime(2014, 4, 5, 9, 35, 0), datetime(2014, 4, 5, 12, 55, 0)))

    itinerary = Itineray(flights)

    print(itinerary.get_total_travel_time())

    print(itinerary.get_total_flight_time())

    
if __name__ == "__main__":
    main()
