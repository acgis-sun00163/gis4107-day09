# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        world_pop_explorer_tests.py
#
# Purpose:     Test functions for functions in world_pop_explorer.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
# ------------------------------------------------------------------------------

import sys
import inspect
import world_pop_explorer as wpe
reload(wpe)

# Copy/paste/change the expected, actual, and call to print_test_results
# from template_for_test_functions below where:
#
#    - expected = Expected result from calling the function
#    - actual = Actual result from calling the function
#    - func = Function being tested (the actual function, not the name)
#
# See test_get_continents_first_in_list as an example.
# Note:  This test may fail as you work through this exercise.  Update as
#        required.
# If you create your own tests, the test function name must
# begin with the word "test"

def template_for_test_functions():
    """Doc string to describe test function"""
    expected = ""
    actual = ""
    print_test_results(func, expected, actual)

# ------------------------------------------------------------------------------

def test_get_continents_Asia_first_in_list():
    """Test Asia is first continent in list"""
    expected = "Asia"
    actual = wpe.get_continents()[2]
    print_test_results(wpe.get_continents, expected, actual)

def test_get_country_count():
    """Get country count from population list"""
    expected = 233
    actual = wpe.get_country_count()
    print_test_results(wpe.get_country_count, expected, actual)

def test_conv_num_with_commas():
    """Test for conversion of text 1,000 to number 1000"""
    number_text = '1,403,500,365'
    expected = 	1403500365
    actual = wpe.conv_num_with_commas(number_text)
    print_test_results(wpe.conv_num_with_commas, expected, actual)


def test_get_top_five_countries():
    """Test for top five countries where China is 1st and Brazil 5th"""
    expected = ['China','India', 'United States', 'Indonesia', 'Brazil']
    actual = wpe.get_top_five_countries()
    print_test_results(wpe.get_top_five_countries, expected, actual)


def test_set_country_populations_dict():
    """Test for the country Réunion"""

    expected = ('1,409,517,397', '+0.4%')
    actual = wpe.set_country_populations_dict().get('China')
    print_test_results(wpe.set_country_populations_dict, expected, actual)

def test_get_population():
    """Test for the country Réunion"""
##    country_name = 'China'
##    expected = 1409517397
##    actual = wpe.get_population(number_text)
##    print_test_results(wpe.get_population, expected, actual)
    pass

def test_get_continents():
    """Test for number of continents"""
    expected = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
    actual = wpe.get_continents()
    print_test_results(wpe.get_continents, expected, actual)

def test_get_continent_populations():
    """Test for population of Asia being larger than 4.5B"""
    expected = {'Europe': 743253404, 'Oceania': 40690786, 'Africa': 1256268025, 'Asia': 4503248822L, 'Americas': 1006801064}
    actual = wpe.get_continent_populations()
    print_test_results(wpe.get_continent_populations, expected, actual)


# ------------------------------------------------------------------------------
# main() and testing helper functions  - safely ignore the rest of this script
# ------------------------------------------------------------------------------

def main():
    """Find and call all functions that begin with 'test'
    """
    test_funcs = get_test_functions()
    for test_func in test_funcs:
        test_func()


def get_test_functions():
    """Returns a list of functions that begin with the word test in the order
       they appear in this file."""

    test_funcs = [obj for name,obj in inspect.getmembers(sys.modules[__name__])
                     if (inspect.isfunction(obj) and name.startswith('test'))]
    src = inspect.getsource(sys.modules[__name__])
    lines = src.split('\n')

    # Create a dictionary with key=function name and value is 0-based order
    # in the module
    ordered_func_names = dict()
    ordered_funcs = list()
    func_index = 0
    for line in lines:
        if line.find("def test") > -1 and not line.find('line.find') > -1:
            func_name = line.split("(")[0].split()[1]
            ordered_func_names[func_name] = func_index
            # Create an empty list with sampe number of elements as test
            # functions
            ordered_funcs.append('')
            func_index += 1
    for test_func in test_funcs:
        index = ordered_func_names[test_func.__name__]
        ordered_funcs[index] = test_func
    return ordered_funcs


def print_test_results(func_tested, expected, actual):
    """func_tested is the function being tested
       expected = Expected result of test
       actual = Actual result of test """

    if not callable(func_tested):
        raise Exception("{} is not a function".format(func_tested))

    func_name = func_tested.__name__
    desc = func_tested.__doc__

    if expected == actual:
        print "PASSED : {}".format(func_name)
        print "__doc__: {}".format(desc)
    else:
        print "FAILED : {}".format(func_name)
        print "__doc__:   {}".format(desc)
        print "Expect : {}".format(expected)
        print "Actual : {}".format(actual)
    print ""

if __name__ == '__main__':
    main()
