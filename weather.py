import turtle

T = turtle.Screen()
if MaxTemp == MinTemp:
	r = 1
	b = 1
else:
	r = (CurrTemp - MinTemp)/(MaxTemp - MinTemp)
	b = (MaxTemp - CurrTemp)/(MaxTemp - MinTemp)
T.bgcolor(r, 0, b)
input()