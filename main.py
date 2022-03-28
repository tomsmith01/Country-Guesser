import random

#store countries and information in dictionary
countries_dict = {}

#populate the dictionary with country and population key pairs
def get_countries_from_file():
    with open('countries.txt') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split(' | ')
            population = get_population_from_line(parts[len(parts) - 1])
            countries_dict[parts[1]] = population
            

#get a random country from the dictionary
def get_random_country():
    #TODO implement here
    country = random.choice(list(countries_dict.keys()))
    return country

#get an integer value of the country population
def get_population_from_line(line):
    words = line.split()
    pop = words[0].translate({ord(','): None})
    if 'million' in line:
        removed_dec_pop = float(pop)*100
        return int(removed_dec_pop)*10000
    return int(pop)

