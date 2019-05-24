rest_time = 2

while True:
	password = input('歡迎進入密碼重設頁面: ')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼錯誤 ! 還有',rest_time,'次機會')
		rest_time = rest_time - 1 
		if rest_time < 0:
			print('錯誤達三次，系統自動關閉')
			break
