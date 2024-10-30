def describe_city(city, country='The United States of America'):
    """accepts the name of a city and its country"""
    print(f"{city.title()} is in {country.title()}.")

describe_city('Dallas')

describe_city('Fort Wayne')

describe_city('Venice',country='Italy')