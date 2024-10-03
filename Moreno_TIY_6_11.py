cities = {
    'new york city':            {
        'country':      'america',
        'population':   '8.8 million',
        'fun fact':     'i have been on tour there',
    },

    'guatemala city': {
        'country':      'guatemala',
        'population':   '3.2 million',
        'fun fact':     'i got to ride a motorcycle there',
    },

    'dallas': {
        'country':      'america',
        'population':   '1.3 million',
        'fun fact':     'i used to live there',
    },
}

for city, infos in cities.items():
    city = city.title()
    country = infos['country'].title()
    population = infos['population'].title()
    fun_fact = infos['fun fact'].title()
    print(f"{city}:")
    print(f"\tCountry: {country}")
    print(f"\tPopulation: {population}")
    print(f"\tFun Fact: {fun_fact}")
    print('\n')