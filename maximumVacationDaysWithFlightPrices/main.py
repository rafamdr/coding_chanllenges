# Given an origin, start date, length nad budget for a trip, find the flights a user can take do maximise the trip -
# i.e., take the longest possible round trip (final destination is the same as origin) using the flights in the dataset.
# For example, given:
#       - Origin: Amsterdam
#       - Start date: Sep 10
#       - Max number of days: 15
#       - Budget: €5000
#
# Flights dates and prices:
#
# ----------------------------------------------
# | ORIGIN    |  DEST.    |  DATE  |  PRICE(€) |
# ----------------------------------------------
# | Amsterdam | Paris     | Sep 10 |    150    |
# | Paris     | London    | Sep 15 |    200    |
# | Paris     | Lisbon    | Sep 14 |     40    |
# | Lisbon    | Amsterdam | Sep 20 |    100    |
# | Lisbon    | London    | Sep 17 |    100    |
# | London    | Amsterdam | Sep 21 |    200    |
# ----------------------------------------------
#
# Accommodation prices
#
# ----------------------------------------------
# | LOCATION  |       PRICE PER NIGHT(€)       |
# ----------------------------------------------
# | Paris     |              300               |
# | London    |              500               |
# | Lisbon    |              200               |
# ----------------------------------------------
#
# The output should be:
#   Sep 10, Paris
#   Sep 14, Lisbon
#   Sep 17, London
#   Sep 21, Amsterdam
#
# The output should be:
#   Sep 10, Paris          150
#   Sep 14, Lisbon         (300 * 4) + 40
#   Sep 17, London         (200 * 3) + 100
#   Sep 21, Amsterdam      (500 * 4) + 200
#
# Total:
#       11 days            4290 euros
# ----------------------------------------------------------------------------------------------------------------------


from typing import List, Dict
from datetime import datetime
# ----------------------------------------------------------------------------------------------------------------------


class Solution:
    # V = Number of locations
    # E = Number of flights
    # I'm not using an adjacency matrix, so time complexity is O(|V| + |E|)
    # Given that I'm keeping track of visited nodes, my Queue can grow up to max number of vertices, so |V| but I'm
    # building a graph that has a space complexity of O(|V| + |E|)
    def __init__(self, flights: List, accommodation_prices: Dict):
        self.graph = {}
        self.curr_year = datetime.now().year
        for origin, destination, fdate, fprice in flights:
            if origin not in self.graph:
                self.graph[origin] = {}
            if destination not in self.graph:
                self.graph[destination] = {}
            fdate_number = datetime.strptime(fdate + ' ' + str(self.curr_year), '%b %d %Y').timetuple().tm_yday
            self.graph[origin][destination] = {'price': fprice, 'day': fdate_number}

        for location in accommodation_prices:
            if location in self.graph:
                self.graph[location]['accom_price'] = accommodation_prices[location]

    def test_trip_constraints(self, origin: str, start_date: str, max_days: int, budget: int) -> List[str]:
        sdate = datetime.strptime(start_date + ' ' + str(self.curr_year), '%b %d %Y').timetuple().tm_yday
        visited = {}
        stack = [
            # [origin, 0, 0, sdate, ['%s - %s' % (start_date, origin)]] # If you want to include origin into the path
            [origin, 0, 0, sdate, []]
        ]
        result_path = []
        result_values = [0, 0]
        while len(stack) > 0:
            current_city, current_cost, current_days, year_day, path = stack.pop()
            visited[current_city] = year_day
            if current_days > 0 and current_city == origin:
                if current_days > result_values[1]:
                    result_path = path.copy()
                    result_values = [current_cost, current_days]
                del visited[current_city]
            else:
                for next_city in self.graph[current_city]:
                    if next_city != 'accom_price':
                        if next_city == origin or next_city not in visited:
                            next_city_flight_price = self.graph[current_city][next_city]['price']
                            next_city_flight_day = self.graph[current_city][next_city]['day']
                            diff_days = (next_city_flight_day - year_day)
                            temp_current_cost = current_cost + next_city_flight_price
                            if 'accom_price' in self.graph[current_city] and diff_days > 0:
                                temp_current_cost += self.graph[current_city]['accom_price'] * diff_days
                            temp_current_days = current_days + diff_days
                            if (
                                    temp_current_cost <= budget and
                                    current_days <= temp_current_days <= max_days
                            ):
                                ext_date = datetime.strptime(
                                    str(self.curr_year) + "-" + str(next_city_flight_day), "%Y-%j"
                                ).strftime("%b %d")
                                item_path = '%s - %s' % (ext_date, next_city)
                                stack.append([next_city, temp_current_cost, temp_current_days,
                                              next_city_flight_day, path + [item_path]])

        return result_path
# ----------------------------------------------------------------------------------------------------------------------


examples = [
    {
        'Flights': [
            ['Amsterdam', 'Paris', 'Sep 10', 150],
            ['Paris', 'London', 'Sep 15', 200],
            ['Paris', 'Lisbon', 'Sep 14', 40],
            ['Lisbon', 'Amsterdam', 'Sep 20', 100],
            ['Lisbon', 'London', 'Sep 17', 100],
            ['London', 'Amsterdam', 'Sep 21', 200],
        ],
        'AccommodationPrices': {
            'Paris': 300,
            'London': 500,
            'Lisbon': 200,
        },
        'InputTests': [
            {
                'Origin': 'Amsterdam',
                'StartDate': 'Sep 10',
                'MaxNumberOfDays': 15,
                'Budget': 5000,
                'ExpectedResult': [
                    'Sep 10 - Paris',
                    'Sep 14 - Lisbon',
                    'Sep 17 - London',
                    'Sep 21 - Amsterdam'
                ]
            },
        ]
    },
]

for ex in examples:
    sol = Solution(ex['Flights'], ex['AccommodationPrices'])
    for input in ex['InputTests']:
        print(
            'Ref...: %s : %s' % (
                str(input['ExpectedResult']),
                str(sol.test_trip_constraints(input['Origin'], input['StartDate'], input['MaxNumberOfDays'],
                                              input['Budget']))
            )
        )
    print()
# ----------------------------------------------------------------------------------------------------------------------
