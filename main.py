from linked_class import MySet
from myclass import my_numbers, my_numbers_child

a = my_numbers(1, 9)
b = my_numbers(7, 3)
c = my_numbers_child(4,5,6)
d = my_numbers_child(9,5,7)

s1 = MySet()
s1.add(a)
s1.add(c)
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
s1.add('Hello')

s2 = MySet()
s2.add(b)
s2.add(d)
s2.add(1)
s2.add(2)
s2.add(3)
s2.add(5)
s2.add('DSA')

s3 = MySet()
s3.add(a)
s3.add(b)
s3.add(c)
s3.add(d)

s4 = MySet()
s4.add(a)
s4.add(b)
s4.add(c)
s4.add(d)

s5 = MySet()

print('--------------------------------------------')
print('Chaking if s2 contains 5: ', s2.contains(5))
print('Chaking if s1 contains 5: ', s1.contains(5))
print('--------------------------------------------')
print('Chaking if s1 is empty: ', s1.isEmpty())
print('Chaking if s5 is empty: ', s5.isEmpty())
print('--------------------------------------------')
print('The length of set s1:', s1.length())
s1.remove(2)
s1.remove(a)
print('The length of set s1 after remove() methods:', s1.length())
print('--------------------------------------------')
print('Checking if s1 is equals to s2:',s1.equals(s2))
print('Checking if s3 is equals to s4:',s3.equals(s4))
print('--------------------------------------------')
print('The union of s1 and s2:', end=' ') 
print(s1.union(s2).print_set())
print('--------------------------------------------')
print('The difference between s1 and s2:', end=' ') 
print(s1.difference(s2).print_set())
print('The difference between s2 and s1:', end=' ') 
print(s2.difference(s1).print_set())
print('--------------------------------------------')