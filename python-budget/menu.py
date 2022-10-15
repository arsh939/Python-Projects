from inspect import BoundArguments
from budget import Budget
from addingStuff import AddingStuff



class Menu(Budget,AddingStuff):
    def __init__(self, income):
        super().__init__(income)

    def menu(self):
        print('——— Welcome to Your Budget ———')

        text = f'What would you like to do?\n1. Add a New Category\n2. Move Money into Category from Income\n3. Move Money from Category into Another Category\n4. View Budget\n5. Delete Category\n6. Exit\n'

        user_answer = input(text)

        while True:
            #add a category
            if user_answer == '1':
                user_dict_ = {}
                user_dict_['category'] = input('what is the category\n')
                user_dict_['amount'] = 0
                #add category is used to add the user to the csv
                self.add_category(user_dict_)
                #this resets the user answer to text
            #move money with income
            #take the money from one of the categories, and then use that money to put it into another category
            elif user_answer == '2':
                #here we are looping through the csv
                for i in self.categories:
                    category = i['category']
                    print(category)
                #show the categories to the users
                user_category = input('choose a category from above\n')
                user_amount = input('choose a whole number amount less than the money you have free\n')

                self.moving_money_income(user_category,user_amount)
            #move category moneys
            elif user_answer == '3':
                for i in self.categories:
                    category = i['category']
                    money = i['amount']
                    print(f'{category} is a category with {money} Dollars')
                user_category = input('choose category to take from\n')
                user_amount = input('choose a whole number amount\n')
                user_new_category = input('choose category to add to\n')
                self.move_money_category(user_category,user_amount,user_new_category)
            #show categories/ turns into show budget eventually
            elif user_answer == '4':
                self.show_budget()

            
            elif user_answer == '5':
                for i in self.load_csv():
                    category = i['category']
                    print(category)
                #show the categories to the users
                user_category = input('choose a category from above\n')
                self.delete_expense(user_category)
            elif user_answer == '6':
                print('thank you come again')
                break

            else:
                print('that is not an option')
                user_answer = input(text)

            user_answer = input(text)

            


    

