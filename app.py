import database

MENU_PROMPT = '''-- Gastronomic guide --

Please choose one of these options:

1) Add a new dish
2) See all dishes
3) Find a dish by name
4) See where is dish origined
5) Exit

Your selection: '''


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != '5':
        if user_input == '1':
            name = input('Enter dish name: ')
            cuisine = input('Where did you try it? ')
            rating = int(input('Enter your rating score(0-100): '))
            database.insert_dish(connection, name, cuisine, rating)
        elif user_input == '2':
            dishes = database.get_everything(connection)

            for dish in dishes:
                print(f'{dish[1]} {dish[2]} {dish[3]}/100')
        elif user_input == '3':
            name = input('Enter dish name to find: ')
            dishes = database.get_by_name(connection, name)
            for dish in dishes:
                print(f'{dish[1]} {dish[2]} {dish[3]}/100')
        elif user_input == '4':
            name = input('Enter your dish: ')
            find_cuisine = database.get_by_cuisine(connection, name)
            print(f'The origin country of the {name} is {find_cuisine[2]}')
        else:
            print('Invalid input, please try again.')

menu()



