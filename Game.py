from SelectCountry import SelectCountry
countries_dict = {}
select = SelectCountry(countries_dict)
select.get_countries_from_file()

#print information to user about population upon incorrect guess
def give_population_hint(guess_country, mys_population):
    guess_population = countries_dict[guess_country]
    if mys_population > guess_population:
        print('Population of mystery Country ↑')
    if mys_population == guess_population:
        print('Population of mystery Country =')
    if mys_population < guess_population:
        print('Population of mystery Country ↓')

#print information to user about name length upon incorrect guess
def give_name_hint(guess_country, mys_country):
    guess_len = len(guess_country)
    mys_len = len(mys_country)

    if mys_len > guess_len:
        print('Length of Country name ↑')
    if mys_len == guess_len:
        print('Length of country name =')
    if mys_len < guess_len:
        print('Length of Country name ↓')

#print information to the user about continent upon incorrect guess
def give_continent_hint(guess_con, mys_con):
    if guess_con == mys_con:
        print("Continent is correct")
    else:
        print("Continent is incorrect")


#main game loop
def play():
    num_tries = 6
    game_won = False

    mys_country = select.get_random_country()
    mys_population = countries_dict.get(mys_country)[0]
    mys_con = countries_dict.get(mys_country)[1]
    print(mys_country)
    while num_tries >= 0 and game_won == False:
        if num_tries == 0:
            print(f"No more guesses remaining. Correct Country was {mys_country}")
            return

        guess_country = input("Guess a country: ")
        guess_pop = countries_dict.get(guess_country)[0]
        guess_con = countries_dict.get(guess_country)[1]
        print(f'Your Guess: {guess_country}, Population: {guess_pop}, Continent: {guess_con}')

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
        give_name_hint(guess_country, mys_country)
        give_continent_hint(guess_con, mys_con)
        num_tries = num_tries - 1

play()
