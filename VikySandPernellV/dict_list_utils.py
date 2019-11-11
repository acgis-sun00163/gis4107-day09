# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------

def main():
    pass

def func(params):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""
    pass

def get_missing_keys(dict_ref, dict_to_compare)：

    exclude = []
    for item in dict_ref.keys():
        for item not in dict_to_compare.keys():
            exclude.append(item)
        return exclude
 
 


        
def get_missing_keys_with_count(dict_ref,dict_to_compare):
    

    exclude = []
    count = 0
    for item in dict_ref.keys():
        for item not in dict_to_compare.keys():
            exclude.append(item)
            count += 1
        return count, exclude
 

 
def get_unique(in_list):
    unique_list = []
    for i in in_list:
        if i not in unique_list:
            unique_list.append(i)
            
    return unique_list

def flatten_list(in_list):

#The list of lists

    flattened_list = []

#flatten the lis
    for x in in_list:
        for y in x:
            flattened_list.append(y)

if __name__ == '__main__':
    main()