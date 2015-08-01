import unittest
from functools import wraps


def multiplicator(method=None, rate=10):
    def decorator(method):
        @wraps(method)
        def wrapper(*args, **kwargs):
            return rate*method(*args, **kwargs)
        return wrapper
    if callable(method):
    	return decorator(method)
    return decorator


class DecoratorTestCase(unittest.TestCase):

	def test_decorator_w_brackets(self):
		
		@multiplicator()
		def f():
			return 1;

		self.assertEqual(f(), 10);

	def test_decorator_wo_brackets(self):
		
		@multiplicator
		def f():
			return 1;

		self.assertEqual(f(), 10);

	def test_decorator_w_params(self):
		
		@multiplicator(rate=5)
		def f():
			return 1;

		self.assertEqual(f(), 5);


if __name__ == '__main__':
    unittest.main()