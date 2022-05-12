def get_hotel_info(hotel_name):
    hotel_info = {
        "Lakewood": {
            "rating": 3,
            "regular": {"week": 110, "weekend": 90},
            "reward": {"week": 80, "weekend": 80},
        },
        "Bridgewood": {
            "rating": 4,
            "regular": {"week": 160, "weekend": 60},
            "reward": {"week": 110, "weekend": 50},
        },
        "Ridgewood": {
            "rating": 5,
            "regular": {"week": 220, "weekend": 150},
            "reward": {"week": 100, "weekend": 40},
        },
    }

    return hotel_info[hotel_name]

def get_cheapest_quotes(week_days, client_type):
    hotels = ["Lakewood", "Bridgewood", "Ridgewood"]

    hotels_quotes = {}

    for hotel in hotels:
        hotels_quotes[hotel] = 0
        hotel_rates = get_hotel_info(hotel)
        for day in week_days:
            if day in ["sat", "sun"]:
                hotels_quotes[hotel] += hotel_rates[client_type]["weekend"]
            else:
                hotels_quotes[hotel] += hotel_rates[client_type]["week"]
    
    cheapest_quote = min(hotels_quotes.values())
    cheapest_hotels = [hotel for hotel in hotels_quotes.keys() if hotels_quotes[hotel] == cheapest_quote]

    return cheapest_hotels

def check_quotes(cheapest_quotes):
    hotel_ratings = [get_hotel_info(hotel)["rating"] for hotel in cheapest_quotes]
    
    best_hotel = cheapest_quotes[hotel_ratings.index(max(hotel_ratings))]

    return best_hotel

def get_cheapest_hotel(number):  # DO NOT change the function's name
    input = number.split(sep = ":")

    client_type = input[0].lower()
    if client_type == "rewards":
        client_type = "reward"

    dates = input[1].split(sep = ",")
    week_days = [date[11:-1] for date in dates]

    cheapest_quotes = get_cheapest_quotes(week_days, client_type)
    
    if len(cheapest_quotes) > 1:
        cheapest_hotel = check_quotes(cheapest_quotes)
    else:
        cheapest_hotel = cheapest_quotes[0]
    
    return cheapest_hotel
