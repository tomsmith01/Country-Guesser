from SelectCountry import SelectCountry
countries_dict = {}
select = SelectCountry(countries_dict)
select.get_countries_from_file()

#print information to user about population upon incorrect guess
def give_population_hint(guess_country, mys_population):
    guess_population = countries_dict[guess_country]
    if mys_population > guess_population:
        print(f'Population of mystery Country is higher than {guess_population}.')
    if mys_population == guess_population:
        print(f'Population of mystery Country is {guess_population}')
    if mys_population < guess_population:
        print(f'Population of mystery Country is less than {guess_population}')

#print information to user about name length upon incorrect guess
def give_name_hint():
    #TODO implement
    pass


def play():
    num_tries = 6
    game_won = False

    mys_country = select.get_random_country()
    mys_population = countries_dict.get(mys_country)
    print(mys_country)
    while num_tries >= 0 and game_won == False:
        if num_tries == 0:
            print("No more guesses remaining.")
            return

        guess_country = input("Guess a country: ")

        #country guessed correctly
        if guess_country == mys_country:
            print("Correct!")
            game_won == True
            return

        #guessed country does not exist
        if countries_dict.get(guess_country) == None:
            print("Country does not exist.")
            num_tries = num_tries - 1

        give_population_hint(guess_country, mys_population)
        num_tries = num_tries - 1

play()
