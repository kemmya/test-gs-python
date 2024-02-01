from lib.gratitudes import *

""" 
Initially, the output is an empty list
"""
def test_initially_empty_list():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []

""" 
when we add something
To be grateful for
"""
def test_add_one_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("I am grateful for my Family")
    assert gratitudes.gratitudes == ["I am grateful for my Family"]

""" 
when we add multiple things
To be grateful for
"""
def test_add_multiple_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("I am grateful for my Family")
    gratitudes.add("I am grateful for my Friends")
    gratitudes.add("I am grateful for my life")
    assert gratitudes.gratitudes == ["I am grateful for my Family", "I am grateful for my Friends", "I am grateful for my life"]

""" 
When we join things to be 
grateful for together
"""

def test_format():
    gratitudes = Gratitudes()
    gratitudes.add("I am grateful for my Family")
    gratitudes.add("I am grateful for my Friends")
    gratitudes.add("I am grateful for my life")
    assert gratitudes.format() == "Be grateful for: I am grateful for my Family, I am grateful for my Friends, I am grateful for my life"