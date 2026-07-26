"""The function below can verify if an ISBN code is valid or not"""

def is_valid(isbn): 
    """Here comes the magic:)"""
    isbn_no_dashes = isbn.replace("-", "")
    sum_for_check = 0
    
    if len(isbn_no_dashes) != 10: 
        return False 
    
    for char_index, char_value in enumerate(isbn_no_dashes):
        if char_value.isdigit() == False and char_index != (len(isbn_no_dashes)-1):
            return False
        if char_value.isdigit() == False and char_index == (len(isbn_no_dashes)-1) and char_value != "X":
            return False
        
        if char_value == "X":
            int_char_value = 10
        else:
            int_char_value = int(char_value)
            
        index_weight = 10 - char_index
        sum_for_check += int_char_value * index_weight   

    if sum_for_check % 11 == 0:
        return True
    else: 
        return False