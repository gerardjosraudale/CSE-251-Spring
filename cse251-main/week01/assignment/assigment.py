'''
Time Guesstimate to complete:
Proficient with all the "Know how to" statements:                       1 hour
Familiar with the "Know how to" statements, but need to review a few:   1 - 4 hours
Need to review most the "Know how to" statements:                       4 - 8 hours
Need to review/relearn all the "Know how to" statements:                8+ hours

All ASSERTS must pass. Everything in this assignment should have been learned
previously. If there are holes in your knowledge, then this is the time to 
fill them (meaning learn the concepts). Take the time to learn by reading
the provided links. There are no group "prove" assignments in this class.

Make sure to write comments above your functions, explaining in your own
words what the functions does. Your comments are your "digital signature",
showing that you both wrote the code and understand how it works.

Grading:
Not passing an assert or answering #10 and #12: 0 points (code must pass all asserts--this is only true of this first assignment)
'''

from unittest import TestCase
from cse251functions import *
from PIL import Image, ImageDraw, ImageFont
# 1) TODO write a function called 'perform_math' that takes three parameters:
# Function to perform mathematical operations

def perform_math(initial_value, value, operation):
    if operation == "+":
        return initial_value + value
    elif operation == "-":
        return initial_value - value
    elif operation == "*":
        return initial_value * value
    elif operation == "/":
        return initial_value / value
    elif operation == "//":
        return initial_value // value
    elif operation == "**":
        return initial_value ** value

# 2) TODO write a function called 'find_word_index' that takes two parameters:
# Function to find the index of a word in a list

def find_word_index(word_to_find, words):
    return words.index(word_to_find)

# 3) TODO write a function called 'get_value_from_dict_using_key' that takes two parameters:
# Function to get a value from a dictionary using a key

def get_value_from_dict_using_key(key, word_dict):
    return word_dict[key]

# 4) TODO write a function called 'get_list_of_urls_from_dict' that takes two parameters:
# Function to get a list of URLs from a dictionary using a key

def get_list_of_urls_from_dict(key, url_dict):
    return url_dict[key]

# 5) TODO write a function called 'find_url' that takes two parameters:
# Function to find a URL containing a specific name within a list of URLs

def find_url(urls, name):
    for url in urls:
        if name in url:
            return url
    return ""


# 6) TODO write a function called 'find_str_in_file' that takes two parameters:
# Function to find a string within a file

def find_str_in_file(filename, str_to_find):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if str_to_find in line:
                    return True
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False
    return False



# 7) TODO write a class called 'MyParentClass'. The constructor should take three parameters:
# Parent class definition

class MyParentClass:
    def __init__(self, value, values, name):
        self.value = value
        self.values = values
        self.name = name

    def get_value_using_index(self, index):
        return self.values[index]



# 8) TODO write a class called 'MyChildClass'. The class should extend the MyParentClass.
# Child class definition

class MyChildClass(MyParentClass):
    def __init__(self, value, values, name, age):
        super().__init__(value, values, name)
        self.age = age


# 9) TODO write a function called 'pass_by_reference_mutable_example' that takes two parameters:
# Function to demonstrate pass-by-reference with mutable objects

def pass_by_reference_mutable_example(lists_are_passed_by_reference_and_mutable, str_to_add):
    lists_are_passed_by_reference_and_mutable.append(str_to_add)
    return lists_are_passed_by_reference_and_mutable[0]

#      10) TODO: Provide a quick explanation of what pass-by-reference means. Also, what does mutable mean?
# pass-by-reference means that the reference to a variable is passed to a function, allowing modifications 
# to be visible outside the function. Mutable refers to the ability of an object or data structure to be modified, allowing changes to its state after creation.

# 11) TODO write a function called 'pass_by_reference_immutable_example' that takes two parameters:
# Function to demonstrate pass-by-reference with immutable objects

def pass_by_reference_immutable_example(strings_are_pass_by_reference_and_immutable, str_to_add):
    strings_are_pass_by_reference_and_immutable += str_to_add
    return strings_are_pass_by_reference_and_immutable
#      12) TODO: What does immutable mean?
# Immutable refers to an object or data structure that cannot be modified or changed after it is created.

# Don't change any of the assert lines. All asserts should pass. You should see "All tests passed!" if all assert pass.
# If an assert doesn't pass, you will see an AssertionError (see https://www.w3schools.com/python/ref_keyword_assert.asp).
# The AssertionError will show you why it didn't pass (meaning, it is not an error with the assertion code, but with your code)

def main():
    ''' Know how to:
        - Call a function
        - Pass in parameters to a function in the correct order
        - Use correct parameter data types
        - Return a value from a function
        - Return correct data type from a function
        - Return from all call paths in a a function
        - Write an IF statement
        - Reading: https://www.geeksforgeeks.org/python-functions/
    '''
    assert perform_math(10, 1, "+") == 11
    assert perform_math(1, 10, "+") == 11
    assert perform_math(10, 1, "-") == 9
    assert perform_math(1, 10, "-") == -9
    assert perform_math(10, 2, "*") == 20
    assert perform_math(2, 10, "*") == 20
    assert perform_math(10, 2, "/") == 5
    assert perform_math(2, 10, "/") == 0.2
    assert perform_math(10, 3, "//") == 3
    assert perform_math(3, 10, "//") == 0
    assert perform_math(10, 3, "**") == 1000
    assert perform_math(3, 10, "**") == 59049

    ''' Know how to:
        - Use a list
        - Use the index function on a list
        - Reading: https://www.geeksforgeeks.org/python-lists/
    '''
    assert find_word_index("a", ["a", "b", "c", "h"]) == 0
    assert find_word_index("b", ["a", "b", "c", "h"]) == 1
    assert find_word_index("c", ["a", "b", "c", "h"]) == 2
    assert find_word_index("h", ["a", "b", "c", "h"]) == 3

    ''' Know how to:
        - Use a dictionary
        - Use a key to get the value in a dictionary
        - Understand that a dictionary value can be list
        - Know how to get the list using a key
        - Know how to write a FOR loop
        - Know how to use "in" keyword
        - Reading: https://www.geeksforgeeks.org/python-dictionary/
    '''
    word_dict = {"k1": 1, "k2": 2, "k3": 3, "k4": 10}
    assert get_value_from_dict_using_key("k1", word_dict) == 1
    assert get_value_from_dict_using_key("k2", word_dict) == 2
    assert get_value_from_dict_using_key("k3", word_dict) == 3
    assert get_value_from_dict_using_key("k4", word_dict) == 10
    movie_dict = {"people": ["http://127.0.0.1:8790/1", "http://127.0.0.1:8790/2", "http://127.0.0.1:8790/3"], "films":
                  ["http://127.0.0.1:8790/film1", "http://127.0.0.1:8790/film2", "http://127.0.0.1:8790/film3"]}
    urls = get_list_of_urls_from_dict("films", movie_dict)
    url = find_url(urls, "film3")
    assert url != None

    '''
        - Know how to make a Python Class
        - Know how to write a constructor
        - Know how to make attributes in a constructor
        - Understand how to use "self" in Python
        - Know how to instantiate an object of a class (shown below)
        - Know how to obtain the value using the object's attribute (shown below)
        - Know what a method is and how to write one
        - Know how to return a value from a method
        - Know to obtain a value at a specific index in a list
        - Know how to extend a class
        - Understand that an extended/child class inherits everything from parent class
        - Readings: https://www.geeksforgeeks.org/python-classes-and-objects/, https://www.geeksforgeeks.org/extend-class-method-in-python/, https://realpython.com/python-super/
    '''
    # 13) TODO instantiate an object using MyParentClass with the following three parameters: (1, [5, 6, 7], "3")
    
    obj = MyParentClass(1, [5, 6, 7], "3")
    # Ensure the assertions pass
    assert obj.value == 1
    assert obj.values == [5, 6, 7]
    assert obj.name == "3"
    assert obj.get_value_using_index(0) == 5
    assert obj.get_value_using_index(1) == 6
    assert obj.get_value_using_index(2) == 7
    
    # 14) TODO instantiate an object using MyChildClass with the following four parameters: (1, [5, 6, 7], "3", 10).
    # 15) TODO: do NOT duplicate the code in the parent class when writing the child class. For example, the parent
    # class constructor already creates the value, values, and name parameters. Do not write these in the child
    # class. Instead, the child constructor should call the parent constructor. Same for the 'get_value_using_index'
    # function, do not rewrite this in the child class.
    childObj = MyChildClass(1, [5, 6, 7], "3", 10)
    assert childObj.value == 1
    assert childObj.values == [5, 6, 7]
    assert childObj.name == "3"
    assert childObj.age == 10
    assert childObj.get_value_using_index(0) == 5
    assert childObj.get_value_using_index(1) == 6
    assert childObj.get_value_using_index(2) == 7
    assert isinstance(childObj, MyParentClass) == True

    '''
        - Know how to open a file
        - Know how to read lines from a file
        - Understand how to compare strings
        - Readings: https://www.geeksforgeeks.org/open-a-file-in-python/, https://www.geeksforgeeks.org/with-statement-in-python/
    '''
    assert find_str_in_file("/Users/joshraudales/GitHub/CSE 251 Spring/cse251-main/week01/assignment/data.txt", "g") == True
    assert find_str_in_file("/Users/joshraudales/GitHub/CSE 251 Spring/cse251-main/week01/assignment/data.txt", "1") == False

    '''
        - Know the difference between pass-by-reference and pass-by-value.
        - Reading: https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference (read the first answer)
        - Technically python is pass-by-object-reference, if you are intested in the difference, read https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/
    '''
    l = ["abc", "def", "ghi"]
    pass_by_reference_mutable_example(l, "jkl")
    assert len(l) == 4
    assert l[3] == "jkl"
    s = "strings are immutable"
    new_string = pass_by_reference_immutable_example(
        s, " so adding to it creates a new object in memory")
    assert id(s) != id(new_string)
    assert len(new_string) != len(s)

    print("All tests passed!")

    
if __name__ == '__main__':
    main()
    
def create_signature_file():
    # Open a new blank image
    img = Image.new('RGB', (400, 100), color='white')

    # Initialize the drawing context
    draw = ImageDraw.Draw(img)

    # Specify font path (or use default font)
    font_path = "path/to/your/font.ttf" 

    # Load font (or use default font)
    try:
        font = ImageFont.truetype(font_path, 14)
    except OSError:
        font = ImageFont.load_default()

    # Add text to the image
    draw.text((10, 10), "Josue Raudales", font=font, fill='black')

    # Save the image
    img.save("signature.png")

# Call the function to create the signature file
create_signature_file()