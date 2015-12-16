#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Comprehensions"""


from data import FRUIT


def get_cost_per_item(shoplist):
    """This function shows the prices of fruit individually.

    Args:
        shoplist(dict): dict of the shopping list

    Returns:
        dict key is the fruit and value is the price

    Example:
        >>> print shoplist
        {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}
        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24,
        'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}

    """
    return {fname: FRUIT[fname]*shoplist[fname]
            for fname in shoplist.iterkeys() if fname in FRUIT}


def get_total_cost(shoplist):
    """This function adds the sum of the prices per fruit

    Args:
        shoplist(dict): dict of the shopping list

    Returns:
        total cost of fruit if valid in data file

    Example:
        >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    """
    mysum = sum(price for price in get_cost_per_item(shoplist).itervalues())
    return mysum
