import sys
sys.path.append('../src')
from math import (add, add_with_bug, calculate_tax_with_bug, calculate_tax)

def test_add():
    assert add(2,2) ==  4
    print('test add')
def test_with_bug():
    assert add_with_bug(0,0) == 0
    assert add_with_bug(1,1) == 1
    #assert add_with_bug(2,3) == 5
    print('test add_with_bug')
def test_duplicated():
    assert add(2,3) == 2+3
    print('test duplicated')
def test_reasonable():
    assert add(2,2) == 4
    assert add(0,0) == 0
    assert add(4,5) == 9
    assert add(-10,1) == -9
    print('test reasonable')
def test_commutative():
    assert add(2,-2) == 0
    assert add(-2,2) == 0
    print('test commutative')

def test_tax_calculation_with_bug():
    try:
        assert calculate_tax_with_bug(1000) == 150
        assert calculate_tax_with_bug(100) == 15
        assert calculate_tax_with_bug(10) == 1.5
        assert calculate_tax_with_bug(1) == 0.15
        assert calculate_tax_with_bug(0) == 0
    except:
        print("Tax Calculation failed")
def test_tax_calculation():
    assert calculate_tax(1000) == 150
    assert calculate_tax(100) == 15
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(13) == 1.95
    print("Tax Calculation test complited")
if __name__ == '__main__':
    test_add()
    test_with_bug()
    test_duplicated()
    test_reasonable()
    test_commutative()
    test_tax_calculation()
    test_tax_calculation_with_bug()
