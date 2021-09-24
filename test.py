import pytest
@pytest.mark.parametrize('s', ["DSsDasds", "sadsd", "DDDDDBB"])
def test_islower_string_eng(s):
    b = True
    for i in range(len(s)):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
            b = False
            break
    assert b == s.islower()


def test_clear_dict():
    d = {'dict': 1, 'dictionary': 2}
    d_clear = {}
    d.clear()
    assert d == d_clear


def test_int_str_concatenation():
    i = 1
    s = '123124'
    try:
        assert i + s
    except TypeError:
        pass

