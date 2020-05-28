import pytesseract as pt
import pyautogui as pg
import sys
import json

colors = {'HEADER' : "",
    'OKBLUE' : "",
    'RED' : "",
    'OKYELLOW' : "",
    'GREEN' : "",
    'LIGHTBLUE' : "",
    'WARNING' : "",
    'FAIL' : "",
    'ENDC' : "",
    'BOLD' : "",
    'UNDERLINE' : "" }

def gather_data(location):
	try:
		l = [""]
		t = int(input("Enter the number of questions"))
		print(colors['OKYELLOW']+"[+] Please wait while collecting data....")
		print("[+] Collecting data. Please do not touch the mouse or keyboard until it is done!"+colors['ENDC'])
		for i in range(t):
			image = pg.screenshot()
			text = pt.image_to_string(image)
			pg.click(location)
			l.append(text)
			print(colors['LIGHTBLUE']+"\rCollecting Question "+str(i+1),end=" ")
			sys.stdout.flush()
		print("\n[+] Data collected successfully.. Saving data.."+colors['ENDC'])
		f = open("questions.json","w")
		json.dump(l, f)
		return l
	except:
		print(colors['FAIL']+"[!] Somehow program Crashed! Saving the collected data..."+colors['ENDC'])
		f = open("questions.json","w")
		json.dump(l, f)
		return l

def answerQueries(l):
	s = input(colors['GREEN']+"[+] Enter the keywords to search. Press CTRL + C to quit>> "+colors['ENDC'])
	for i in range(len(l)):
		if s in l[i]:
			print(colors['OKYELLOW']+"Found Match in "+str(i)+colors['ENDC'])

def detect_save_and_submit():
	image = "button.png"
	location = pg.locateCenterOnScreen(image),confidence=0.5)
	if location==None:
		print(colors['FAIL']+"[!] Could not detect Save & Next Button..\n[!] Please make sure it is visible on the screen."+colors['ENDC'])
		tryagain = input(colors['GREEN']+"[+] Do you want to try again(Y/N)?"+colors['ENDC'])
		if tryagain in "yY":
			return detect_save_and_submit()
		else:
			return None
	print(colors['GREEN']+"[+] Next button found at "+str(location))
	print("[+] Now move to the first question"+colors['ENDC'])  # and wait while collecting data.
	pg.moveTo(location)
	return location

if __name__=="__main__":
	query = input(colors['GREEN']+"[+] Welcome! Please login to the exam and open terminal & browser in split screen mode. Make Sure that Questions and Save&Next Button are visible.\n"+colors['ENDC']+colors['OKYELLOW']+"[+] Hit Enter once done that."+colors['ENDC'])
	isFirstTime = input(colors['LIGHTBLUE']+"[+] Is it a new exam or you have already saved any data before(Enter 1 or 2)?"+colors['ENDC'])
	l = []
	if isFirstTime == "1":
		print("[+] Creating new Exam....Done!")
		print("[+] Detecting Save & Next Button....")
		saveandnext = detect_save_and_submit()
		if saveandnext==None:
			print("[-] Exiting the program...")
			exit(0)
		
		l = gather_data(saveandnext)
		print("[+] Now you can enter the queries..")
		print(colors['WARNING']+"[!] Note that if the program was crashed, it won't answer all the queries.."+colors['ENDC'])
	else:
		print("[+] Detecting already save files...")
		try:
			f = open("questions.json","r")
			l = json.load(f)
		except:
			print(colors['FAIL']+"[!] Could not find any file... Exiting.."+colors['ENDC'])
			exit(0)
	try:
		while True:
			answerQueries(l)
	except KeyboardInterrupt:
		print("\n[+] Quitting the program...")

		





