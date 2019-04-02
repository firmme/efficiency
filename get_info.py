import win32clipboard as cb
import win32con
import re

#支持HS机房和TM机房
# cb.EmptyClipboard()
# cb.SetClipboardData(win32con.CF_TEXT, "Hello World!")  #复制文本内容到剪贴板，系统后台会返回内存地址
def theGigabit(text):
	search_ip = re.search( r'IP.*Address.*:(.*)', text, re.I)
	search_aip = re.search( r'Additional.*IP.*:(.*)', text, re.I)
	search_lan_ip = re.search( r'LAN.*IP.*:(.*)', text, re.I)
	search_port = re.search( r'port.*:(.*)', text, re.I)
	search_username = re.search( r'login.*:(.*)', text, re.I)
	search_password = re.search( r'password.*:(.*)', text, re.I)
	text = ''
	if search_ip:
		text += 'IP地址: '+search_ip.group(1)+'\n'
		if search_aip:
			text += '附加IP: '+search_aip.group(1)+'\n'
		if search_lan_ip:
			text += '内网IP: '+search_lan_ip.group(1)+'\n'
		text += '端口: '+search_port.group(1)+'\n'
		text += '账号: '+search_username.group(1)+'\n'
		text += '密码: '+search_password.group(1)+'\n'
		text = text.replace(' ','')
		text = text.replace('/',' / ')
		text = text.replace(':',': ')
		cb.OpenClipboard()
		cb.EmptyClipboard()
		cb.SetClipboardData(win32con.CF_TEXT, text.encode(encoding='gbk'))
		cb.CloseClipboard()	
	else:
		print ("No match!!")


def hs(text):
	search_ip = re.search( r'外网IP.*：.*\s{1,2}([\d\.]*)\s{1,2}([\d\.]*)', text, re.I)
	search_username = re.search( r'系统账号.*：(.*)', text, re.I)
	search_password = re.search( r'系统密码.*：(.*)', text, re.I)
	text=''
	if search_ip:
		text += '主IP:'+'\n'+search_ip.group(1)+'\n'+search_ip.group(2)+'\n'
		text += '账号:'+search_username.group(1)+'\n'
		text += '密码:'+search_password.group(1)+'\n'
		text = text.replace(' ','')
		text = text.replace('/',' / ')
		text = text.replace(':',': ')
		print(text)
		cb.OpenClipboard()
		cb.EmptyClipboard()
		cb.SetClipboardData(win32con.CF_TEXT, text.encode(encoding='gbk'))
		cb.CloseClipboard()	
	else:
		print ("No match!!")



def remote_conn(text):
	pass


def newtheGigabit(text):
	search_ip = re.search( r'Main IP Address.*:(.*)', text, re.I)
	search_aip = re.search( r'.*Additional IP.*:(.*)', text, re.I)
	search_lan_ip = re.search( r'LAN.*IP.*:\s*([0-9\.]*)', text, re.I)
	search_port = re.search( r'.*RDP Port.*:(.*)', text, re.I)
	search_username = re.search( r'Admin.*Login.*:(.*)', text, re.I)
	search_password = re.search( r'[AL].*Password.*:(.*)', text, re.I)
	text = ''
	if search_ip:
		text += '主IP: '+search_ip.group(1)+'\n'
		if search_aip:
			text += '副IP: '+search_aip.group(1)+'\n'
		if search_lan_ip:
			if len(search_lan_ip.group(1))>5:
				text += '内IP: '+search_lan_ip.group(1)+'\n'
		text += '端口: '+search_port.group(1)+'\n'
		text += '账号: '+search_username.group(1)+'\n'
		text += '密码: '+search_password.group(1)+'\n'
		text = text.replace(' ','')
		text = text.replace('/',' / ')
		text = text.replace(':',': ')
		print(text)
		cb.OpenClipboard()
		cb.EmptyClipboard()
		cb.SetClipboardData(win32con.CF_TEXT, text.encode(encoding='gbk'))
		cb.CloseClipboard()	
	else:
		print ("No match!!")


def jiuhe(text):
	search_ip = re.search( r'主机IP地址：\s([\d\.]*)', text, re.I)
	search_serverinfo1 = re.search( r'编号＆别名：\s#(\d*)', text, re.I)
	search_serverinfo2 = re.search( r'服务器节点：\s\D*(\d*)', text, re.I)
	search_sys = re.search( r'操作系统：\s(.*)', text, re.I)
	search_password = re.search( r'root初始密码：(\w*)', text, re.I)
	text = ''
	if search_ip:
		text += 'TM-TG-'+search_serverinfo2.group(1)+'\t'+search_serverinfo1.group(1)+'\n'
		text += '主IP: '+search_ip.group(1)+'\n'
		print(search_sys.group(1),search_sys.group(1).find('windows'))
		if search_sys.group(1).find('windows') != -1:
			text += '端口: '+'3389'+'\n'
			text += '账户: '+'Administrator'+'\n'
		else:
			text += '端口: '+'22'+'\n'
			text += '账户: '+'root'+'\n'

		text += '密码: '+search_password.group(1)+'\n'
		text = text.replace(' ','')
		text = text.replace(':',': ')
		print(text)
		cb.OpenClipboard()
		cb.EmptyClipboard()
		cb.SetClipboardData(win32con.CF_TEXT, text.encode(encoding='gbk'))
		cb.CloseClipboard()	
	else:
		print ("No match!!")


# input('press enter to exit....')
# 
# 
if __name__ =="__main__":
	cb.OpenClipboard()
	text= cb.GetClipboardData(win32con.CF_TEXT).decode(encoding='gbk') #'Hello World!'
	cb.CloseClipboard()
	if re.search("外网",text,re.I):
		hs(text)
	elif re.search("云主机信息",text,re.I):
		jiuhe(text)
	else:
		newtheGigabit(text)




# username:s:MyUserName 
# domain:s:MyDomain 
# alternate shell:s: 
# shell working directory:s:
# password 51:b:密码（加密后）



#pip install pypiwin32

# import win32crypt
# import binascii

# pwdHash = win32crypt.CryptProtectData("your password string".encode('utf-16-le'),'psw',None,None,None,0)
# print(binascii.hexlify(pwdHash).upper())

# os.system('MSTSC /v 103.106.244.106:3389 /admin')