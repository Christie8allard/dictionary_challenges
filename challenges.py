import csv

def grocery_calculator(groceries: dict):
    """A function to add up grocery bills.

    Arguments:
        - groceries: a dict which has the names of grocery bill items as its 
        keys, and the cost of the items as its values.

    Returns: a float representing the total cost of the grocery bill.

    Example input: {
        "Baby Spinach 100g bag": 2.78,
        "Hot Chocolate 300g": 3.70,
        "Crackers 250g packet": 2.10,
        "Coffee 500g": 9.00,
        "Carrots 1kg bag": 0.56,
        "Oranges 1kg bag": 3.08
    }

    Example output: 21.22
    """
    def grocery_calculator(groceries: dict) -> float:
        total_cost = sum(groceries.values())
        return total_cost
    
    groceries = {
        "Baby Spinach 100g bag": 2.78,
        "Hot Chocolate 300g": 3.70,
        "Crackers 250g packet": 2.10,
        "Coffee 500g": 9.00,
        "Carrots 1kg bag": 0.56,
        "Oranges 1kg bag": 3.08
    }

    total = grocery_calculator(groceries)
    print(total)

def word_counter(word_list: list):
    """A function to count the occurrences of each word in a word list.

    Arguments: 
        - word_list: a list of strings

    Returns: a dictionary containing the number of occurrences of each word in
    word_list.

    Example input: ["apple", "banana", "apple", "cherry", "apple", "banana"]

    Example output: {"apple": 3, "banana": 2, "cherry": 1}
    """
    def word_counter (word_list: list): 
        word_count = {}
        for word in word_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count

    word_list = {
        "apple":0, "banana":1 , "apple":2 , "cherry":3 , "apple":4 , "banana":5
    }
    return word_counter



def create_colour_dict(file_path: str):
    """A function that accesses an indicated csv file of colour values and 
    converts it into a dictionary.
    
    Arguments:
        - file_path: a string representing the location of a .csv file
        
    Returns: a dictionary whose keys are the plain English names of the colours
    described in the .csv file, and whose values are the hex codes of those 
    colours.
    
    Example input: "./colours_3_very_simple.csv"
    Example output: {"White": "#FFFFFF", "Black": "#000000", "Red": "#FF0000"}
    """
import csv

def create_colour_dict(file_path: str):
    colour_dict = {}

    with open('colours_3_very_simple.csv') as csv_file:
        csv_reader=csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        colour_name = row['English']
        hex_code = row['Hex']
        colour_dict['colour_name'] = hex_code
    
    return colour_dict

        