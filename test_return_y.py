@pytest.mark.parametrize("input1, input2, expected", [
    ([1,2,2,3], [3],[4.0])])
def test_return_y(input1, input2, expected):
    from return_y import return_y
    answer = return_y(input1, input2)
    assert answer == expected

@pytest.mark.parametrize("input, expected", [
    ([1,2,2,3], [1,1])])
def test_return_y_slope(input, expected):
    from return_y import find_slope_b
    answer1, answer2 = find_slope_b(input)
    assert answer == expected