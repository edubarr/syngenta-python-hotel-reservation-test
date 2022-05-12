def get_hotel_info(hotel_name):
    '''Takes a string with the hotel name, and returns all the info about the hotel (rating and price rates).'''

    #Dict of hotel infos
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
    '''Takes a list of week (and weekend) days and the type of the client and return a list of cheapest hotels (one or more)'''

    hotels = ["Lakewood", "Bridgewood", "Ridgewood"]

    hotels_quotes = {}

    # Loop through all hotels for every day of the list and saves the total quote on the hotels_quotes dict
    for hotel in hotels:
        hotels_quotes[hotel] = 0
        hotel_rates = get_hotel_info(hotel)
        for day in week_days:
            if day in ["sat", "sun"]:
                hotels_quotes[hotel] += hotel_rates[client_type]["weekend"]
            else:
                hotels_quotes[hotel] += hotel_rates[client_type]["week"]
    
    # Chooses the cheapest hotels on the dict and return a list
    cheapest_quote = min(hotels_quotes.values())
    cheapest_hotels = [hotel for hotel in hotels_quotes.keys() if hotels_quotes[hotel] == cheapest_quote]

    return cheapest_hotels

def check_quotes(cheapest_quotes):
    '''Check the list of cheapest hotels and return the best of them based on the rating'''

    hotel_ratings = [get_hotel_info(hotel)["rating"] for hotel in cheapest_quotes]
    
    best_hotel = cheapest_quotes[hotel_ratings.index(max(hotel_ratings))]

    return best_hotel

def get_cheapest_hotel(number):  # DO NOT change the function's name
    # Split the input into the type of client and days of reservation
    input = number.split(sep = ":")

    # Takes the type of client and convert to needed format
    client_type = input[0].lower()
    if client_type == "rewards":
        client_type = "reward"

    # Split the string that contains all dates into a list of dates and takes only the week day part into another list
    dates = input[1].split(sep = ",")
    week_days = [date[11:-1] for date in dates]

    # Get cheapest quotes from the function
    cheapest_quotes = get_cheapest_quotes(week_days, client_type)
    
    # Check if have more than one cheapest quote, and get best hotel
    if len(cheapest_quotes) > 1:
        cheapest_hotel = check_quotes(cheapest_quotes)
    else:
        cheapest_hotel = cheapest_quotes[0]
    
    return cheapest_hotel
