import sys
sys.path.append('../src')
from math import (add, add_with_bug)
def test_add():
    assert add(2,2) == 4
    assert add_with_bug(0,0) == 0
    assert add_with_bug(1,1) == 1
    #assert add_with_bug(2,3) == 5
    print('test complited')
if __name__ == '__main__':
    test_addiction()
