def city_country(city='santiago', country='chile'):
    """takes the name of a city and its country"""
    city_country_pair = f"{city.title()}, {country.title()}"
    return city_country_pair

default_pair = city_country()
print(default_pair)

pair_1 = city_country('dallas', 'the united states of america')
print(pair_1)

pair_2 = city_country('venice', 'italy')
print(pair_2)