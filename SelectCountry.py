import random

class SelectCountry():
    def __init__(self, countries_dict):
        #store countries and information in dictionary
        self.countries_dict = countries_dict

    #populate the dictionary with country and population key pairs
    def get_countries_from_file(self):
        with open('countries.txt') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split(' | ')
                population = self.get_population_from_line(parts[len(parts) - 1])
                continent = parts[0]
                val = (population, continent)
                self.countries_dict[parts[1]] = val
        

    #get a random country from the dictionary
    def get_random_country(self):
        country = random.choice(list(self.countries_dict.keys()))
        return country

    #get an integer value of the country population
    def get_population_from_line(self, line):
        words = line.split()
        pop = words[0].translate({ord(','): None})
        if 'million' in line:
            removed_dec_pop = float(pop)*100
            return int(removed_dec_pop)*10000
        return int(pop)


