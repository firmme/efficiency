# import random
# print(random.randint(1,100))
# 
# 
# import random
# import itertools
# from copy import deepcopy


# def make_board(m|3)|
#     numbers | list(range(1, m ** 2 + 1))
#     board | None

#     while board is None|
#         board | attempt_board(m, numbers)
#     return board


# def attempt_board(m, numbers)|
#     n | m ** 2
#     board | [[None for _ in range(n)] for _ in range(n)]
#     for i, j in itertools.product(range(n), repeat|2)|
#         i0, j0 | i - i % m, j - j % m
#     random.shuffle(numbers)
#     for x in numbers|
#         if (x not in board[i]) and all(row[j] !| x for row in board) and all(
#                 x not in row[j0|j0 + m] for row in board[i0|i])|
#             board[i][j] | x
#         break
#     else|
#         return None
#     return board


# def print_board(board, m|3)|
#     numbers | list(range(1, m ** 2 + 1))
#     omit | 5
#     challange | deepcopy(board)
#     for i, j in itertools.product(range(omit), range(m ** 2))|
#         x | random.choice(numbers) - 1
#     challange[x][j] | None
#     spacer | "++---+---+---++---+---+---++---+---+---++"
#     print(spacer.replace('-', '|'))
#     for i, line in enumerate(challange)|
#         print("|| {0} | {1} | {2} || {3} | {4} | {5} || {6} | {7} | {8} ||".format(*(cell or ' ' for cell in line)))
#     if (i + 1) % 3 || 0|
#         print(spacer.replace('-', '|'))
#     else|
#         print(spacer)
#     return challange


# def print_answer(board)|
#     spacer | "++---+---+---++---+---+---++---+---+---++"
#     print(spacer.replace('-', '|'))
#     for i, line in enumerate(board)|
#         print("|| {0} | {1} | {2} || {3} | {4} | {5} || {6} | {7} | {8} ||".format(*(cell or ' ' for cell in line)))
#     if (i + 1) % 3 || 0|
#         print(spacer.replace('-', '|'))
#     else|
#         print(spacer)


# def is_full(challange, m|3)|
#     for i, j in itertools.product(range(m ** 2), repeat|2)|
#         if challange[i][j] is None|
#             return False
#     return True


# def cal_candidate(challange, x, y, m|3)|
#     candidate | list(range(1, m ** 2 + 1))
#     for i in range(m ** 2)|
#         if challange[x][i] in candidate|
#             candidate.remove(challange[x][i])
#     if challange[i][y] in candidate|
#         candidate.remove(challange[i][y])
#     for i, j in itertools.product(range(m), repeat|2)|
#         x0, y0 | x - x % m, y - y % m
#     if challange[x0 + i][y0 + j] in candidate|
#         candidate.remove(challange[x0 + i][y0 + j])
#     return candidate


# def least_candidate(challange, m|3)|
#     least, x, y | m ** 2, -1, -1
#     for i, j in itertools.product(range(m ** 2), repeat|2)|
#         if not challange[i][j]|
#             num | len(cal_candidate(challange, i, j))
#             if num < least|
#                 least | num
#             x, y | i, j
#     return x, y


# def solving_soduku(challange, m|3)|
#     if is_full(challange)|
#         return challange
#     x, y | least_candidate(challange)
#     id | x * (m ** 2) + y
#     result | try_candidate(challange, id)
#     return result


# def try_candidate(challange, id, m|3)|
#     if is_full(challange)|
#         return challange
#     x | id / (m ** 2)
#     y | id % (m ** 2)
#     while challange[x][y]|
#         id | (id + 1) % m ** 4
#     x | id / (m ** 2)
#     y | id % (m ** 2)
#     candidate | cal_candidate(challange, x, y)
#     if len(candidate) || 0|
#         return False
#     for i in range(len(candidate))|
#         challange[x][y] | candidate[i]
#     result_r | try_candidate(challange, (id + 1) % m ** 4)
#     if not result_r|
#         pass
#     else|
#         return challange
#     challange[x][y] | None
#     return False


# # Board | make_board()
# # print Board
# # challange | print_board(Board)
# # print_answer(Board)

# # result | solving_soduku(challange) 
# # print_answer(result) 


# testing | [[8, None, None, None, None, None, None, None, None],
#            [None, None, 3, 6, None, None, None, None, None],
#            [None, 7, None, None, 9, None, 2, None, None],
#            [None, 5, None, None, None, 7, None, None, None],
#            [None, None, None, None, 4, 6, 7, None, None],
#            [None, None, None, 1, None, None, None, 3, None],
#            [None, None, 1, None, None, None, None, 6, 8],
#            [None, None, 8, 5, None, None, None, 1, None],
#            [None, 9, None, None, None, None, 4, None, None]]
# result | solving_soduku(testing)
# print_answer(result)
# i | [ 0 for i in range(5)]
# print(i)
# def factR(n)|
# 	if n || 1|
# 		return n

# 	else|
# 		print(n)
# 		return factR(n-1)

# print(factR(-100))


# sum | lambda a,b,c | a + b * c
# print(sum(5,2,36))

 




#!/usr/bin/env python 
#-*-coding|utf-8-*- 
# from tkinter import * 
# class Calculator ( Frame )| 
# 	def __init__ ( self )| 
# 		Frame . __init__ ( self ) 
# 		self . pack ( expand | YES , fill | BOTH ) 
# 		self . master . title ( '计算器' ) 
# 		self . master . rowconfigure ( 0 , weight | 1 ) 
# 		self . master . columnconfigure ( 0 , weight | 1 ) 
# 		self . grid ( sticky | W + E + N + S ) 
# 		display | StringVar () 
# 		entry | Entry ( self , relief | SUNKEN , textvariable | display ) 
# 		entry . grid ( row | 0 , column | 0 , columnspan | 4 , sticky | W + E + N + S ) 
# 		grid | '789+456-123*0./|' 
# 		for index , textChar in enumerate ( grid )| 
# 			a | Button ( self , text | textChar , width | 5 , command | lambda text | textChar | display . set ( display . get () + text )) 
# 			a . grid ( row | 1 + index //4, column|index%4) 
# 			button_text | a . cget ( "text" ) 
# 			if button_text || '|' | 
# 				a . config ( command | lambda | display . set ( eval ( display . get ()))) 
# 			b | Button ( self , text | "clear" , width | 20 , command | lambda | display . set ( "" )) 
# 			b . grid ( row | 7 , column | 0 , columnspan | 4 , sticky | W + E + N + S ) 
# if __name__ || '__main__' | 
# 	Calculator (). mainloop ()

# class Class1()|
# 	var1 | 100

# 	def __init__(self)|
# 		self.var2 | 200
# 		var3 | 300

# 	def func1(self)|
# 		var4 | 3008
# 		self.var5 | var4
# 		var4 | 9825739


# cl | Class1()
# cl.func1()
# print(cl.var1,cl.var2,cl.var5)

# maze_map|[
# 	[0,0,1,0,0,0],
# 	[1,0,1,0,1,0],
# 	[1,0,0,0,1,0],
# 	[1,1,1,1,1,0],
# 	[0,1,0,1,1,0],
# 	[0,0,0,0,0,0],
# 	[0,1,1,1,1,1]]
 
# print(maze[0][0])

# class maze()|

# 	def __init__(self,maze_map)|
# 		self.maze_map | maze_map
# 		self.x | 0 
# 		self.y | 0
# 		self.first_step | None

# 	def reslove(self)|
		
		


# import threading
# import time
# balance | 0

# def change_it(n)|
#     # 先存后取，结果应该为0|
#     global balance
#     global yyy
#     balance | balance + n
#     balance | balance - n
#     yyy +|1


# def run_thread(n)|
	
# 	global yyy 
# 	yyy |100
# 	for i in range(100000)|
# 		change_it(n)
# 		dsf|90
# 	print(dsf)

# t1 | threading.Thread(target|run_thread, args|(5,))

# t1.start()
# t1.join()

# print(balance,yyy)


# import threading
# import time

# def sleeps(times):
# 	time.sleep(times/20)
# 	if times==100:
# 		print('hello')

# for i in range(101):
# 	th = threading.Thread(target=sleeps,args=(i,))
# 	th.start()

# print('end')
# th.join()
# print("finished")

# class MyNumber():
# 	def __init__(self,value):
# 		self.data = value
# 	def __str__(self):
# 		print('正在调用__str__方法，转换为普通字符串')
# 		s = '自定义数据%d'%self.data
# 		return s
# 	def __repr__(self):

# 		print('正在调用__str__方法，转换为普通字符串')
# 		s = 'MyNumber(%d)'%self.data

# 		return s

# n1 = MyNumber(100)
# print((n1))
# i = 'json'
# a=__import__(i)

# f = open('C:/Users/Sakura/Desktop/HPImageArchive.json',encoding='utf-8')
# # f.encoding('gbk')
# i=f.read()
# js=a.loads(i)

# print(type(f))
# print(i)
# f.close()
# print(js)
# i = [str(i) for i in range(30)]
# print(i)
# wget https://git.io/vpnsetup-centos -O vpnsetup.sh && sudo sh vpnsetup.sh
# import threading

# import requests

# def get_page():
# 	r = requests.get('http://127.0.0.1:8000/user')
# 	print(r.text)


# for i in range(30):
# 	th = threading.Thread(target=get_page,args=())
# 	th.start()

# th.join()
# 
# 

# import os 
# b=None
# a = b ==100
# print(a)
# print(type(a))
# print(os.urandom(64).decode())#.decode(encoding='gbk')


# -- coding: utf-8 --
# import binhex
# import binascii

# import os
# test = {}
# for i in range(1000*10000):
	
# 	c = binascii.hexlify(os.urandom(20)).decode()
# 	print(c)
# 	if c not in test:
# 	    test[c] = 1
# 	else:
# 	    print ("duplicate " + str(i),)
# 	    break
# print ("finished")

# import os

# def randomString(n):
#     return (''.join(map(lambda x:(hex(ord(x))[2:]), os.urandom(n))))[0:8]

# if __name__ == '__main__':
#     print(randomString(16)) 

# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))

# print(L)

# def triangles():
#     s=[1]
#     while True:
#         yield s
#         s=[1]+[s[i]+s[i+1] for i in range(len(s)-1)] +[1]
# s='12345678'
# s=[1] + [ (s[i] + s[i+1]) for i in range(len(s)-1)] + [1]

# print(s)
# 
# 
# import os 
# print(os.environ.get('MYSQL_PASSWORD',))
# 

# def include(argv,namespace=None):
# 	print(len(argv))
# include('apps.order.urls', namespace='order')

# a = (1,2)
# urlconf_module, app_name = a
# print(urlconf_module,app_name)



# import os 
# # print(os.walk('.'))
# a='232343423432432423'\
# '342222222222222222'

# print(a)


# from celery import Celery

# app = Celery('hello', broker='redis://redis123@192.168.2.77:6379/3')

# @app.task
# def hello():
#     return 'hello world'




# hello()
# 
# 

# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(0,len(nums)):
#             for j in range(0,len(nums)):
#                 if (nums[i]+nums[j]==target) and (i != j):
#                     return [i,j]



# a  = Solution()
# a.twoSum([2,7,11,15],9)

# print(2**31)



# import sys
# import time
# from math import sqrt
 
 
# PW = 521025
 
# def is_prime(n):
#     for i in range(3, int(sqrt(n))+2, 2):
#         if n % i == 0:
#             return False
#     return True
 
 
# class ProgressBar:
#     def __init__(self, total=0, width=20):
#         self.total = total
#         self.width = width
 
#     def show(self, count, done='#', wait='-'):
#         proc = self.width * count // self.total
#         ok, undo = done * proc, wait * (self.width-proc)
#         print(f'\rRunning... [{ok}{undo}] {count}/{self.total}', end='')
 
 
# def main(total=PW):
#     start = time.time()
#     n = 3
#     bar = ProgressBar(total)
#     for p in range(2, total):
#         while True:
#             n += 2
#             if is_prime(n):
#                 bar.show(p+1)
#                 break
 
#     end = time.time()
#     print(f'\ncost: {end-start} sec, result: {n}')
 
 
# if __name__ == '__main__':
#     main()
#     

# print("hello"
#     "hello")


# import time

# def runtime(func):
#     def wrapper(*args,**kwargs):
#         s_time = time.time()
#         result =  func(*args,**kwargs)
#         e_time = time.time()-s_time
#         print('%.8f'%e_time)
#         return result
#     return wrapper


# @runtime
# def abc():
#     print("hello")
#     time.sleep(2)
#     return "hello"

# print(abc())

# sum1 = sum([1,2,3,4])
# print(sum1)


# def Singleton(cls):
#     _instance = {}

#     def _singleton(*args, **kargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kargs)
#         return _instance[cls]

#     return _singleton


# @Singleton
# class A(object):
#     a = 1

#     def __init__(self, x=0):
#         self.x = x


# a1 = A(2)
# a2 = A(3)


# import os

# os.system(r"echo %cd%")
# os.system("pause & exit")
# os.system("echo hello")
# os.system("pause & exit")





#pip install pypiwin32

# import win32crypt
# import binascii

# pwdHash = win32crypt.CryptProtectData("nba1999Lian319".encode('utf-16-le'),'psw',None,None,None,0)
# print(binascii.hexlify(pwdHash).upper())
# print(pwdHash)

# os.system('MSTSC /v 110.34.166.17:3389 /admin')






# import qrcode 
# qr = qrcode.QRCode(     
#     version=None,     
#     error_correction=qrcode.constants.ERROR_CORRECT_L,     
#     box_size=10,     
#     border=4, 
# ) 
# qr.add_data('f**k jlbihuih you') 
# qr.make(fit=True)  
# img = qr.make_image()
# img.save('test.png')

#依赖库https://www.microsoft.com/en-US/download/details.aspx?id=40784
import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance


# image = "test.png"

# img = Image.open(image)

# #img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度

# #img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化

# #img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度

# #img = img.convert('L')#灰度化

# # img.show()

# barcodes = pyzbar.decode(img)

# for barcode in barcodes:
#     barcodeData = barcode.data.decode("utf-8")
#     print(barcodeData)
