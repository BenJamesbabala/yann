"""
Just a dummy test I'm writing to get used to the idea of unittesting. I've never 
written unit tests before, so this is my template for them.
"""
import imp 

def test_progressbar():
    assertTrue(imp.find_module('progressbar'))

def test_skdata():
    assertTrue(imp.find_module('skdata'))

def test_scipy():
    assertTrue(imp.find_module('scipy'))

def test_numpy():    
    assertTrue(imp.find_module('numpy'))

def test_theano():
    assertTrue(imp.find_module('theano'))

def test_yann():
    assertTrue(imp.find_module('yann'))
