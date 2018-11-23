count = 0
say= 0
asal = False

while True:
	say = say + 1
	for i in range(2,say):
		if say % i ==0:
			asal = False
			#print("say = "+str(say)+" i = "+str(i))
			break
		else:
			asal=True
	if asal:
		count = count + 1
		asal = False

		if(count == 10001-1): # -1 var cunku 2 asal oldugu halde dongude yok
			print(say)
			break