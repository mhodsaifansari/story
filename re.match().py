import re
a=input('REG NO.: ')

if re.match('[0-9]{2}[a-zA-Z]{3}[0-9]{4}',a):
	print('valid')
else:
	print('invalid')
