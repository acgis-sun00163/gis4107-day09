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
        if item not in dict_to_compare.keys():
            exclude.append(item)
        return exclude

if __name__ == '__main__':
    main()