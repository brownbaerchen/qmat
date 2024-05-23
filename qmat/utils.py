#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utility module
"""

def checkOverriding(cls, name, isProperty=True):
    method = getattr(cls, name)
    parent = getattr(cls.mro()[-2], name)
    assert method != parent, \
        f"{name} method must be overriden in {cls.__name__} class"
    if isProperty:
        assert type(method) == property, \
            f"{name} method must be a property in {cls.__name__} class"
    else:
        pass
        # TODO : check that signature are the same


def storeAlias(cls, dico, alias):
    assert alias not in dico, f"{alias} alias already registered in {dico}"
    dico[alias] = cls


def storeClass(cls, dico):
    storeAlias(cls, dico, cls.__name__)
    aliases = getattr(cls, "aliases", None)
    if aliases:
        assert isinstance(aliases, list), \
            f"aliases must be a list in class {cls.__name__}"
        for alias in aliases:
            storeAlias(cls, dico, alias)
