import os,time,subprocess
active_devices=[]
global active_devices
def connect():
	process = subprocess.Popen(['adb', 'devices'], stdout=subprocess.PIPE)
	out, err = process.communicate()
	fo=open("devices.txt","w")
	f1=fo.write(out)
	fo.close()
	f2=open('devices.txt','r+')
	f2=f2.readlines()
	return f2
def choose():
	state=True
	while state==True:
		print "YOU HAVE "+str(len(active_devices))+" DIVECES CONNECTED YOUR PC"
		for i in range(len(active_devices)):
			print str(i)+"--> "+active_devices[i]
		print "CHOOSE ANY ONE"
		div=input(">>")
		try:
			device=active_devices[div]
			print device
			state=False
		except :
			print "SORRY ...! \n" 
			state==True
	return device
def main():
	f2=connect()
	if len(f2)<=2:
		state=True
		while state==True:
			print "please connect Android device and wait 10 sec..."
			f2=connect()
			if len(f2)<=2:
				time.sleep(10)
			else:
				for i in f2[1:len(f2)-1]:
					active_devices.append(i.split()[0])
					
				stete=False
				break;
	else:
		for i in f2[1:len(f2)-1]:
			active_devices.append(i.split()[0])
	if len(active_devices) >1:
		device=choose()
	else:
		device=active_devices[0]
		os.system("rm devices.txt")
		return device
if __name__=='__main__':
	main()
