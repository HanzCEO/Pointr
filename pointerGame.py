import mouse, keyboard
from time import sleep
import os, json
from os import system as cmd
from random import randint as random


"""	██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗     ████████╗██╗  ██╗███████╗
	██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    ╚══██╔══╝██║  ██║██╔════╝
	██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║       ██║   ███████║█████╗  
	██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║       ██║   ██╔══██║██╔══╝  
	╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝       ██║   ██║  ██║███████╗
	 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝        ╚═╝   ╚═╝  ╚═╝╚══════╝
"""																													 
#	███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗███████╗     ██████╗ ██████╗ ██████╗ ███████╗                          
#	██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝                          
#	███████╗██║   ██║██║   ██║██████╔╝██║     █████╗      ██║     ██║   ██║██║  ██║█████╗                            
#	╚════██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝      ██║     ██║   ██║██║  ██║██╔══╝                            
#	███████║╚██████╔╝╚██████╔╝██║  ██║╚██████╗███████╗    ╚██████╗╚██████╔╝██████╔╝███████╗                          
#	╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝            


	' ██╗ ██╗  ██╗     ██████╗  ██████╗ ██╗   ██╗'
	'████████╗███║    ██╔════╝ ██╔═══██╗██║   ██║'
	'╚██╔═██╔╝╚██║    ██║  ███╗██║   ██║██║   ██║'
	'████████╗ ██║    ██║   ██║██║   ██║╚██╗ ██╔╝'
	'╚██╔═██╔╝ ██║    ╚██████╔╝╚██████╔╝ ╚████╔╝ '
	' ╚═╝ ╚═╝  ╚═╝     ╚═════╝  ╚═════╝   ╚═══╝  '

"""
v0.1.0:
 - First release
 - Basic game functioned
 - Scoring is OK

v0.1.1:
 Bug Fixes:
  #1 Exitting after winning the game. (Now [space] to start)
 
 - Press [space] to start the game.

v0.1.2:
 Bug Fixes:
  #1 UnboundLocalError: local variable 'theTime' referenced before assignment. (Now variable 'theTime' moved to line 40)

v0.1.3:
 Bug Fixes:
  #1 Clearing the screen after winning the game too fast (not gonna bring the you win text, lol.). (Now, the pause feature after win is live!)
  
v0.2.0:
 - Refresh the data every round or when the game was over
 
v0.3.0:
 - Colors!!
"""

def ClrScrn():
	cmd('cls' if os.name == 'nt' else 'clear')

target = (random(0,1340),random(0,760))
data = []

def game():
	theTime = 0.00
	while True:
		try:
			sleep(.05)
			theTime = theTime + .05
			ClrScrn()
			print("Point your pointer to "+str(target)+" to win the game.")
			print(mouse.get_position())
			print(f"Won\t\t\t: {data[0]}\nSurrender\t\t: {data[1]}\nBest Time Score\t\t: {data[2]}s")
			print(f"Time elapsed: {theTime}s")
			print("Ctrl+C To Surrender")
		except KeyboardInterrupt:
			ClrScrn()
			print("Point your pointer to "+str(target)+" to win the game.")
			print(mouse.get_position())
			print(f"Won\t\t\t: {data[0]}\nSurrender\t\t: {data[1]}\nBest Time Score\t\t: {data[2]}")
			print("Ctrl+C To Surrender")
			mouse.move(x=target[0],y=target[1],duration=3)
			if mouse.get_position() == target:
				print("You win, but work harder!")
				data[1] = str(int(data[1]) + 1)
				f = open('./tempMouse.tmp','w')
				f.write(data[0]+"\n"+data[1]+"\n"+data[2])
				f.close()
				break
		if mouse.get_position() == target:
			print("Win!")
			data[0] = str(int(data[0]) + 1)
			f = open('./tempMouse.tmp','w')
			f.write(data[0]+"\n"+data[1]+"\n"+str(theTime) if theTime < float(data[2]) else data[0]+"\n"+data[1]+"\n"+data[2])
			f.close()
			break
# End game function

while True:
	try:
		ClrScrn()
		try:
			with open('./tempMouse.tmp', 'r') as f:
				data = f.read().split("\n")
		except:
			with open('./tempMouse.tmp', 'w') as f:
				f.write('0\n0\n99999999999999999999999999')
				f.close()
			with open('./tempMouse.tmp', 'r') as f:
				data = f.read().split("\n")
		print("Press [space] to start.\nCtrl+C to exit")
		keyboard.wait('space')
		game()
		print('Press [space] to continue')
		keyboard.wait('space')
	except KeyboardInterrupt:
		exit()