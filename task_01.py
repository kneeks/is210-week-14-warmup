#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Arbitrary arguments"""


from pet import Pet


class Dog(Pet):
    """sub class for pet class."""
    def __init__(self, has_shots=False, **kwargs):
        """ Constructor for Dog class

        Args:
            has_shots(bool): def to False
            **kargs(arb): arb argument dict

        Attibutes
            has_shots(bool): True or def. to False

        """
        self.has_shots = has_shots
        Pet.__init__(self, **kwargs)
