import csv
import pandas as pd
from addingStuff import AddingStuff 

class Budget(AddingStuff):
    def __init__(self, income):
        super().__init__()
        self.income = income


    def add_category(self, dict_):
        self.categories.append(dict_)
        print(self.categories)
        self.write_csv()

    def move_money_category(self, first_category, amount, second_category):
        first_loop = False
        second_loop = False
        # list_categories = []
        # for i in self.categories:
        #     list_categories.append(i['category'])

        if second_category in self.load_csv():
            for first_dict in self.categories:
                if first_category == first_dict['category']:
                    less_amount = int(first_dict['amount'])-int(amount)
                    first_dict['amount'] = str(less_amount)
                    first_loop = True


        if first_category in self.categories:
            for second_dict in self.categories:
                if second_category == second_dict['category']:
                    new_amount = int(second_dict['amount']) + int(amount)
                    second_dict['amount'] = str(new_amount)
                    second_loop = True
            
        if second_loop and first_loop:
            self.write_csv()
        else:
            print('Invalid Entry')

    def moving_money_income(self,category,amount):
        try:    
            not_category = True
            real_amount = int(amount)
            if (real_amount) <= self.income-self.sub_():
                for categories in self.categories:
                    if categories['category'] == category:
                        not_category = False
                        category_amount = int(categories['amount'])
                        category_amount += real_amount
                        categories['amount'] = str(category_amount)
            else:
                print('You dont have enough for that')
            if not_category:
                print('This is not a category')
            self.write_csv()
        except:
            print('invalid entry')

    def show_budget(self):
        print('———— Here is your Budget ————')
        print(f'Your total monthly income is: {self.income} Dollars')
        for i in self.load_csv():
            category = i['category']
            amount = i['amount']
            print(f' {category} || {amount} Dollars')
        print(f'and you have {self.income - self.sub_()} Dollars left')
        print('——— END ———')
    
    def show_money_left(self):
        print(self.income - self.sub_())


        
    
    
