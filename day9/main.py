#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nestinf Dictionary in a Dictionary
travel_log2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 15},
}

#Nesting a dictionary in a List

travel_log = [
    {
        "country": "France",
         "cities_visited": ["Paris", "Lille", "Dijon"],
          "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 15
        },
]