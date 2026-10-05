import time
import json
class Game_helper():
	@staticmethod
	def input_int(*args):
		i="i"
		l=len(args)
		if l >= 1:
			out="\x1b[A\r"+str(args[0])
		else:
			out="\x1b[A\r"
		if l >= 2:
			error="\x1b[A\r"+str(args[1])
		else:
			error="\x1b[A\r"
		print("")
		while i == "i":
			try:
				print("\x1b[A\r"+(" "*100),end="")
				i=int(input("\r"+out))
			except ValueError:
				print(error)
				time.sleep(2)
				i="i"
		return i
	@staticmethod
	def input_float(*args):
		i="i"
		l=len(args)
		if l >= 1:
			out=str(args[0])
		else:
			out=""
		if l >= 2:
			error=str(args[1])
		else:
			error=""
		while i == "i":
			try:
				i=float(input(out).replace(",","."))
			except ValueError:
				print(error)
				i="i"
		return i
	@staticmethod
	def timer(*args):
		print("")
		if len(args) == 2:
			for i in range(args[0],0,-1):
				print("\x1b[A\r"+str(i)+" ")
				time.sleep(1)
			print("\x1b[A\r"+str(args[1])+" ")
		elif len(args) == 1:
			for i in range(args[0],0,-1):
				print("\x1b[A\r"+str(i)+" ")
				time.sleep(1)
			print("\x1b[A\r ",end="")
		else:
			raise TypeError
	@staticmethod
	def random(a,b):
		seed=(a*b)+time.perf_counter()
		time.sleep(0.05)
		seed%=b-a
		time.sleep(0.05)
		seed+=a
		return int(seed)

class App_helper():
	@staticmethod
	def saveApp(*args):
		if len(args) == 2:
			a=f"{args[0]}.json"
			data=args[1]
		elif len(args) == 3:
			a=f"{args[0]}.{args[1]}"
			data=args[2]
		else:
			raise TypeError
		with open(a,"w") as a:
			json.dump(data,a,ensure_ascii=False,indent=4)
	@staticmethod
	def loadApp(*args):
		if len(args) == 1:
			a=f"{args[0]}.json"
		elif len(args) == 2:
			a=f"{args[0]}.{args[1]}"
		else:
			raise TypeError
		try:
			with open(a,"r") as a:
				b=json.load(a)
		except FileNotFoundError:
			return ""
		return b
		
		