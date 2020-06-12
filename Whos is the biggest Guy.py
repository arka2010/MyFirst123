# Make sure to un-comment the function line below when you are done.
# Remember to name your function correctly.
# Write your code here...
def bigger_guy(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def biggest_guy(num1, num2, num3):
    # find bigger guy between num1 and num2
    # find biggest guy between bigger guy and num3
    if num1 > num2:
        bigger_guy = num1
    else:
        bigger_guy = num2

    if bigger_guy > num3:
        biggest_guy = bigger_guy
    else:
        biggest_guy = num3


    return  biggest_guy


# Do not remove lines below here,
# this is designed to test your code.

def test_biggest_guy():
    try:
        assert biggest_guy(1, 3, 2) == 3
        assert biggest_guy(30, 10, 20) == 30
        assert biggest_guy(20, 10, 30) == 30
        assert biggest_guy(2, 1, 9) == 9
        assert biggest_guy('a', 'a', 'b') == 'b'  # 'b' is greater than 'a'
        print('SUCCESS!')
        print("Your CODE is CORRECT")

    except (AssertionError) as e:
        print(e)
        import wrong
        return

    import success

#test your code by un-commenting the line(s) below
test_biggest_guy()
