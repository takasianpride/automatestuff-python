# coding: utf-8

def comma(spam):
    return ', '.join(spam[:-1]) + ', and ' + spam[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']

print(comma(spam))
