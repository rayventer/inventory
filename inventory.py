
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        return self.cost
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        return self.quantity
        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
        return f'Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity},'
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    f = open('inventory.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    j = 0
    for i in lines:
        if j==0:
            print('i')
            j+=1
            pass
        else:
            j+=1
            try:
                print(i)
                data = i.replace('\n', '').split(',') 
                new_object = Shoe(data[0], data[1], data[2], int(data[3]), int(data[4])) #converts text file lines to objects
                shoe_list.append(new_object) #adds object to list
            except Exception:
                print('error')
    
     
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
def capture_shoes():
    country = input('Enter the country: ')
    code = input('Enter the product code: ')
    product = input('Enter the product: ')
    cost = int(input('Enter the cost: '))
    quantity = int(input('Enter the quantity of shoes: '))
    new_shoe_object = Shoe(country, code, product, cost, quantity) 
    shoe_list.append(new_shoe_object)
    f = open('inventory.txt', 'a')
    f.write(f'{country},{code},{product},{cost},{quantity}') #appends new object to text file
        
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    for i in  shoe_list:
        print(i.__str__())
    
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    j = shoe_list[0].quantity
    for i in shoe_list:
        z = i.quantity
        if z <= j:
            lowest = i
            j = z #sorts the quantites and keeps the lowest
    print(lowest.__str__())
    user_input = input('Do you want to add to this quantity? Y/N: ')
    if user_input == 'Y':
        amount_added = int(input("Enter the amount you want to add"))
        for i in shoe_list:
            object_mapping = f'{i.country},{i.code},{i.product},{i.cost},{i.quantity} \n'
            if i == lowest:
                i.quantity+= amount_added
                print('The amount has been added')
            f = open('inventory.txt', 'a', encoding='utf-8')
            for k in shoe_list:
                f.writelines(object_mapping) #rewrites all the lines so that new value can be put in


    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def search_shoe():
    shoe_searched = input('Enter the name of the shoe you want to buy: ')
    for i in shoe_list:
        if shoe_searched == i.product:
            print(i.__str__())
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    for i in shoe_list:
        total_value = i.cost * i.quantity
        print(f' {i.product} {total_value}')
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    j = 0
    for i in shoe_list:
        if i.quantity > j:
            j = i.quantity
            highest_shoe = i #keeps largest qauntity in shoes
    print(highest_shoe.__str__()) #prints largest quantity
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
read_shoes_data() #reads all the data at the start
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
usage_message = '''
Welcome to the email system! What would you like to do?
cs - capture a shoe
rs - restock
ss - search for a shoe
hq - find the highest quantity of shoe
va - view all shoes
vp - value for every shoe
e - exit this program.
'''
while True:
    user_choice = input(usage_message).strip().lower()
    if user_choice == "cs":
        capture_shoes()
    elif user_choice == "rs":
        re_stock()
    elif user_choice == "ss":
        search_shoe()
    elif user_choice == "hq":
        highest_qty()
    elif user_choice == "va":
        view_all()
    elif user_choice == "vp":
        value_per_item()
    
    elif user_choice == "e":
        print('Goodbye!')
        break
    else:
        print("Oops - incorrect input")