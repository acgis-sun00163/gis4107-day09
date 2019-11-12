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

def get_missing_keys(dict_ref, dict_to_compare):
    """Returns a LIST of missing keys
    OR an empty list if no keys are missing."""
##    actual = [1, 3]
##    return actual

    leftovers = []
    for item in dict_ref.keys():
        if item not in dict_to_compare.keys():
            leftovers.append(item)

    return leftovers



if __name__ == '__main__':
    main()