from nose.tools import assert_equal, assert_almost_equal, assert_true, \
    assert_false, assert_raises, assert_is_instance

from mean import mean

def test_mean1():
    obs = mean([0, 0, 0, 0])
    exp = 0
    assert_equal(obs, exp)

    obs = mean([0, 200])
    exp = 100
    assert_equal(obs, exp)

    obs = mean([0, -200])
    exp = -100
    assert_equal(obs, exp)

    obs = mean([0]) 
    exp = 0
    assert_equal(obs, exp)

def test_floating_mean1():
    obs = mean([1, 2])
    exp = 1.5
    assert_equal(obs, exp)

def test_isnotempty():
	assert_raises(ZeroDivisionError, mean, [])
	
def test_isnumlist():
	assert_raises(TypeError, mean, ['1', 'banana', 3])
	assert_raises(TypeError, mean, 'banana')
	assert_raises(TypeError, mean, 1)

def main():
    test_mean1()
    test_floating_mean1()
    test_isnotempty()
    test_isnumlist()
    print "we ran the main"

if __name__ == "__main__":
    main()