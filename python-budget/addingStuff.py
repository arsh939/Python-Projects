import os
import csv
import pandas as pd



class AddingStuff:
    def __init__(self):
        self.categories = self.load_csv()

        
    def load_csv(self):
        arr = []
        path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(path, 'database/expenses.csv')
        
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for dict_ in reader:
                arr.append(dict_)
        
        return arr

    def write_csv(self):
        #takes data as dictionary and turns it into csv
        df = pd.DataFrame.from_dict(self.categories)
        print(df)
        df.to_csv(r'database/expenses.csv', index = False, header = True)


    def sub_(self):
        num = 0
        for category in self.load_csv():
            num += int(category['amount'])
        return num

    def delete_expense(self,name):
        for c in self.categories:
            if c['category'] == name:
                self.categories = [i for i in self.categories if i!=c]
                self.write_csv()



