#!/usr/bin/env python3

LOW_THRESHOLD = 3
LOW_WORD = 'foo'

HIGH_THRESHOLD = 5
HIGH_WORD = 'bar'


def fizzbuzz(value):
	"""
	The fizzbuzz method accepts a number and returns the required response.

	>>> fizzbuzz(5)
	'bar'

	>>> fizzbuzz(8)
	8

	>>> fizzbuzz(9)
	'foo'

	>>> fizzbuzz(15)
	'foobar'

	>>> fizzbuzz(3.14159265)
	3.14159265

	>>> fizzbuzz(u'42')
	Traceback (most recent call last):
	  ...
	ValueError: The value passed must be a number

	>>> fizzbuzz(u'peaches')
	Traceback (most recent call last):
	  ...
	ValueError: The value passed must be a number
	"""
	output = ''

	if type(value) != int and type(value) != float:
		raise ValueError('The value passed must be a number')

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