driving = input ('請問您有開過車嗎?')
age = input ('請輸入您的年齡:')
age = int(age)
if driving == '有':
	if age >= 18:
		print ('你通過測驗了')
	else :
		print ('我要去檢舉你')
elif driving == '沒有' :
	if age >= 18 :
		print ('你可以試試看開車')
	else :
		print ('好小孩')
else :
	print ('只能輸入有or沒有')
