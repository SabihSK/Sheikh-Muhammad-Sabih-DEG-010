from ..sum_func import add, add_positive

# Implement your tests here.

def test_add_2_2():
    assert add(2,2) == 4

def test_add_positive_2_2():
    assert add_positive(2,2) == 4

def test_add_positive_2_2_fp():
    assert add_positive(-2,2) == None

def test_add_positive_2_2_pf():
    assert add_positive(2,-2) == None

def test_add_positive_2_2_ff():
    assert add_positive(-2,-2) == None

def test_add_positive_type_out():
    assert type(add_positive(2,2)) == int
