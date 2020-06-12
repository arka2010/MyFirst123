# Make sure to un-comment the function line below when you are done.
# Remember to name your function correctly.
# WRITE YOUR CODE HERE...
def bigger_guy(num1, num2):
    if num1> num2:
        return num1
    else:
        return num2


# Do not remove lines below here,
# this is designed to test your code.

def test_bigger_guy():
    assert bigger_guy(1, 2) == 2
    assert bigger_guy(10, 20) == 20
    assert bigger_guy(20, 10) == 20
    assert bigger_guy(10, 10) == 10
    assert bigger_guy(2, 1) == 2
    assert bigger_guy('a', 'b') == 'b'  # 'b' is greater than 'a'
    print("YOUR CODE IS CORRECT!")


# test your code by un-commenting the line(s) below
test_bigger_guy()