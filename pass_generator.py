import random
import datetime
import os
import ctypes

os.system("title |Password Generator|")
os.system('color 01a')
date = datetime.datetime.now()
format_date = date.strftime("\n\n%d-%m-%Y  %I:%M:%S %p\n---Password Generator---\t\t\t\t")
print(format_date)
num = ['1','2','3','4','5','6','7','8','9','0']
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower = [x.lower() for x in upper]
specialchar = r'`~!@#$%^&*()_+-=[]{}|/;:,<.>?'
specialchar = list(specialchar)
allchar = upper + lower + specialchar
n = int((input('\n\nEnter length of your password: ')))
#check if input of n < 0
while(n<=0):
	print('Wrong input! The length of your password must larger than 0. Please try again!')
	n = int((input('\n\nEnter length of your password: ')))
password = []

#create simple password.
def _simple(n):          
	for i in range(0, n):
		password.append(random.choice(upper + lower + num))
#create complex password
def _complex(n):
	for i in range(0, n):    
		password.append(random.choice(allchar))

def choice(n):
	ch = eval(input('Press 1 to create simple password\nPress 2 to create complex password\n>'))
	#check if input ch != 1 and != 2
	while(ch != 1 and ch != 2):
		print('Wrong input! Please try again!')
		ch = eval(input('Press 1 to create simple password\nPress 2 to create complex password\n>'))

	if(ch == 1):
		_simple(n)
	if(ch == 2):
		_complex(n)
	
choice(n)

password=''.join(password)

if(len(password) > 0):
	print(('Your generated password is:\n' + password))

#save password to .txt file	
n = input('\n\n\nEnter Filename to save it: ')
fob = open(n + '.txt', 'w+')
fob.write('Your generated password is: \n\n')
fob.write(password)
fob.close()
ctypes.windll.user32.MessageBoxW(0,"Your Password was saved successfully in a text file " + n + ".txt","Message",1)
