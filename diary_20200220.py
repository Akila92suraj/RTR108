Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
Traceback (most recent call last):
  File "/home/user/RTR108/test1.20.02.2020", line 2, in <module>
    true
NameError: name 'true' is not defined
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
Traceback (most recent call last):
  File "/home/user/RTR108/test1.20.02.2020", line 2, in <module>
    true
NameError: name 'true' is not defined
>>> 5==5
True
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
>>> 5==5
True
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
True
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
True
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
True
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
True
False
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
True
False
True
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> type(False)
<class 'bool'>
>>> x =5
>>> y=3
>>> x!=y
True
>>> x>y
True
>>> x<y
False
>>> x<=y
False
>>> x>=y
True
>>> x is y
False
>>> x is not y
True
>>> 17 == x
False
>>> 17 ==54
False
>>> 17 ==5
False
>>> 17 and true
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    17 and true
NameError: name 'true' is not defined
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
True
False
True
Traceback (most recent call last):
  File "/home/user/RTR108/test1.20.02.2020", line 5, in <module>
    print(x>0)
NameError: name 'x' is not defined
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
True
False
True
Traceback (most recent call last):
  File "/home/user/RTR108/test1.20.02.2020", line 5, in <module>
    print(x>0)
NameError: name 'x' is not defined
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
True
False
True
Traceback (most recent call last):
  File "/home/user/RTR108/test1.20.02.2020", line 5, in <module>
    print(x>0)
NameError: name 'x' is not defined
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
True
False
True
True
x is positive
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
True
False
True
False
x is positive
>>> 
================ RESTART: /home/user/RTR108/test1.20.02.2020 ================
False
x is positive
>>> x =3
>>> if x < 10:
	print('šmall')
	File "<stdin>", line 3
	
SyntaxError: invalid syntax
>>> if x < 10:
	print('šmall')
	print('Done')
	File "<stdin>", line 3
	
SyntaxError: invalid syntax
>>> if x % 2 == 0 :
	print(''x is  even')
	      
SyntaxError: invalid syntax
>>> if x%2 ==0 :
	      print ('x is even')
	      else :
	      
SyntaxError: invalid syntax
>>> print ('x is odd')
	      
x is odd
>>> 
================ RESTART: /home/user/RTR108/test120022020.PY ================
x is odd
>>> 
================ RESTART: /home/user/RTR108/test120022020.PY ================
x is odd
>>> 
================ RESTART: /home/user/RTR108/test120022020.PY ================
x is odd
>>> 
================ RESTART: /home/user/RTR108/test120022020.PY ================
x is odd
>>> x= 4
	      
>>> y= 5
	      
>>> if x < y:
	      print('x is less than y')
	      elif x > y
	      
SyntaxError: invalid syntax
>>> if x < y:
	      print('x is less than y')

	
x is less than y
>>> elif x > y :
	      
SyntaxError: invalid syntax
>>> 
================ RESTART: /home/user/RTR108/test120022020.PY ================
x is less than y
>>> 
================ RESTART: /home/user/RTR108/test120022020.PY ================
x is greater than y
>>> 
================ RESTART: /home/user/RTR108/test120022020.PY ================
x and y are equal
>>> 
================ RESTART: /home/user/RTR108/test120022020.PY ================
x and y are equal
Traceback (most recent call last):
  File "/home/user/RTR108/test120022020.PY", line 11, in <module>
    if choice == 'a':
NameError: name 'choice' is not defined
>>> 
