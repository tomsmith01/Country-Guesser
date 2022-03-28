def get_countries_from_file():
    with open('countries.txt') as f:
        lines = f.readlines()

#get an integer value of the country population
def get_population_from_text_line(line):
    words = line.split()
    if 'million' in line:
        return words[0]*1000000
    return words*1
