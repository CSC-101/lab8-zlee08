import group


def test1_groups_of_3():
    result = group.groups_of_3([1,2,3,4,5,6,7,8,9])
    expected = [[1,2,3],[4,5,6],[7,8,9]]
    if result == expected:
        print("Test Passed")
    else:
       print("Test Failed")

test1_groups_of_3()

def test2_groups_of_3():
    result = group.groups_of_3([1,2,3,4,5,6,7,8])
    expected = [[1,2,3],[4,5,6],[7,8]]
    if result == expected:
        print("Test also passed")
    else:
       print("Test failed")

test2_groups_of_3()

