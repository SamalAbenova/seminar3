
class my_numbers:
	def __init__(self, n1 = 0, n2 = 0):
		self.n1 = n1
		self.n2 = n2

	def print_n1n2(self):
		print('n1 = ', self.n1)
		print('n2 = ', self.n2)

	def change_att(self):
		self.n1 = 20
		self.n2 = 25
		print('n1 = ', self.n1)
		print('n2 = ', self.n2)

	def sum_n1n2(self):
		return self.n1 + self.n2

	def mult_n1n2(self):
		return self.n1 * self.n2

class my_numbers_child(my_numbers):
	def __init__(self, n1 = 0, n2 = 0, n3 = 0):
		self.n1 = n1
		self.n2 = n2
		self.n3 = n3

	def n3_square(self):
		return self.n3 ** 2
