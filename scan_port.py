#! /usr/bin/env python
#*-* coding:utf-8 *-*


import socket,time,threading
socket.setdefaulttimeout(5) #超时时长

def socket_port(ip,port):
	try:
		if port >= 65535:
			pirnt('端口扫描结束')
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result=s.connect_ex((ip,port))
		if result==0:
			lock.acquire()
			print(ip,":",port,'端口被占用')
			lock.release()
	except:
		print("端口扫描异常")

def ip_scan(ip):
	try:
		print("开始扫描 %s"%ip)
		start_time=time.time()
		for i in range(0,65534):
			th=threading.Thread(target=socket_port,args=(ip,i))
			th.start()
		th.join()
		print("端口扫描完成,总共用时%.2f"%(time.time()-start_time))
		# input('press enter to exit')

	except Exception as e:
		print("扫描出错: %s"%e)


if __name__ == "__main__":
	# ip=input("input the ip you need to scan:")
	ip="103.113.9.25"
	lock=threading.Lock()
	ip_scan(ip)