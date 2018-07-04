#!/usr/bin/env python
# -*- coding: utf8 -*-


def validator(password):
    if len(password) <= 8 or password.isdigit() or password.isupper():
        return False
    return True
