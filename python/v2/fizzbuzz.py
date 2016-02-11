#!/usr/bin/env python2

LOW_THRESHOLD = 3
LOW_WORD = u'foo'

HIGH_THRESHOLD = 5
HIGH_WORD = u'bar'


def fizzbuzz(value):
	"""
	The fizzbuzz method accepts a number and returns the required response.

	>>> fizzbuzz(5)
	u'bar'

	>>> fizzbuzz(8)
	8

	>>> fizzbuzz(9)
	u'foo'

	>>> fizzbuzz(15)
	u'foobar'

	>>> fizzbuzz(3.14159265)
	3.14159265

	>>> fizzbuzz('42')
	Traceback (most recent call last):
	  ...
	ValueError: The value passed must be a number

	>>> fizzbuzz('peaches')
	Traceback (most recent call last):
	  ...
	ValueError: The value passed must be a number
	"""
	output = ''

	if type(value) != int and type(value) != float:
		raise ValueError(u'The value passed must be a number')

	if not (value % LOW_THRESHOLD):
		output += LOW_WORD

	if not (value % HIGH_THRESHOLD):
		output += HIGH_WORD

	if not len(output):
		output = value

	return output;

if __name__ == '__main__':
	import doctest
	doctest.testmod()
