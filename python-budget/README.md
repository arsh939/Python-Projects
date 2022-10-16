# Python Budget App
## Displaying Choices
The first step is to create a simple interface in which you can 1. Create something 2.  You create a new category 3. You need to be able to move the wealth from one category to the other. Finally, you need to be able to view your budget and where all your money is going 
- - - -
1. Add a new Category
2. Move Money into Category from Income
3. Move Money from Category into Another Category
4. View Budget
5. Delete Category
6. Exit
- - - -
## Menu Class
This is a class that is responsible for displaying the menu options and just overall responsible for the User Interface. I used this class to abstract the Interface and keep all of the complicated logic in the other class **Budget**  and then I just inherit all of the budget logic from this budget class
``` python
class Menu(Budget,AddingStuff):
    
    def __init__(self, income):
        super().__init__(income)

    def menu(self):
        print(‘——— Welcome to Your Budget ———‘)

        text = f"What would you like to do\n1. Add a New Category\n2. Move Money into Category from Income\n3. Move Money from Category into Another Category\n4. View Budget\n5. Delete Category\n6. Exit\n"

        user_answer = input(text)

        while True:

```

## Budget Class
This is where all of the logic that is responsible for accomplishing what the User is asking for. For example. If the user wants to add a category, then they will call the add_category() which is inherited from budget. 
### add_category inheritance
- - - -
budget.py add_category() method
``` python
def add_category(self, dict_):
        self.categories.append(dict_)
        print(self.categories)
        self.write_csv()	
```

- - - -
menu.py calling the add_category method 
``` python
#add a category
if user_answer == '1':
   	user_dict_ = {}
	user_dict_['category'] = input('what is the category\n')
	user_dict_['amount'] = 0
	#add category is used to add the user to the csv
	self.add_category(user_dict_)
	#this resets the user answer to text

```
- - - -
As seen above, the logic for add_category is abstracted away from the menu class in order to make the logic easier, all you need to do is say add_category() and then pass in a dictionary.
- - - -
## addingStuff class
This class is just used to update the csv or to grab information from the csv. In a full stack app, I would be using a database, but for this project I am just using a csv and writing and reading from there. This class is responsible for that work. Below is how adding stuff loads the csv and how it writes to the csv
``` python
 def load_csv(self):
        arr = []
        path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(path, 'database/expenses.csv')
        
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for dict_ in reader:
                arr.append(dict_)
        
        return arr
	#this helps with loading the data from the csv
```
- - - -
``` python
def write_csv(self):
        #takes data as dictionary and turns it into csv
        df = pd.DataFrame.from_dict(self.categories)
        print(df)
        df.to_csv(r'database/expenses.csv', index = False, header = True)

#this writes the new data to the csv. 
```
- - - -
## Conclusion
I think in the end this project is quite nice because I can use my terminal as the interface. Eventually the interface will be created using a front end with a frontend framework, or library such as React, then add a database instead of a csv, and lastly, I will use Django as the backend framework. However, for now I am happy with being able to just have a quick way of looking at where I can put my money and how much money I will have left. 