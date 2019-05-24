
password = 'a123456'
rest_time = 2

while rest_time > 0 :
	pwd = input('歡迎進入密碼重設頁面: ')
	if pwd == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤 ! 還有', rest_time, '次機會')
		rest_time = rest_time - 1 
