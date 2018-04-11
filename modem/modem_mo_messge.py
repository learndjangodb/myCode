import os,time,datetime,csv,random
import device 
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('message_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	os.chdir(mydir)
	cmdr='adb logcat -b radio  > sms_log'+'&'
	os.system(cmdr)
def number():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	numbers=your_list[0]
	return random.choice(numbers[1::])
def message():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	msg=your_list[1]
	return random.choice(msg[1::])

def iterations():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	iters=your_list[2]
	return int(random.choice(iters[1::]))

def test_sms(div,num,text):
	cmd="adb shell input  keyevent 3"
	os.system(cmd)
	cmd1="adb shell am start -a android.intent.action.SENDTO -d sms:"+num
	cmd2="adb shell input text $(echo {} | sed -e 's/ /\%s/g')".format(text)
	time.sleep(10)
	cmd3 = "adb shell input keyevent 22"
	cmd4="adb shell input keyevent 66"
	rc=os.system(cmd1)
	os.system(cmd2)
	os.system(cmd3)
	os.system(cmd4)
	os.system(cmd)
	return rc

def iter_status(ite,div,num,text):
	collect_logs()
	print "This program will execute "+str(ite)+" Iterations"	
	for i in range(ite):
		msg = test_sms(div,num,text)
		if msg == 0:
			print "Test passed"
		else:
			print "Test Failed"

			

div =device.main()
print div,"conncected device"
num = number()
text=message()
print text ,"\n This message is sending .....TO "+num 
iteration=iterations()
iter_status(iteration,div,num,text)
