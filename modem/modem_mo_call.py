import os,time,datetime,csv,random
import device
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('Call_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	os.chdir(mydir)
	cmdr='adb logcat -b radio > Call_log'+'&'  # call Logs
	os.system(cmdr)
def number():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	numbers=your_list[0]
	return random.choice(numbers[1::])
def iterations():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	iters=your_list[2]
	return int(random.choice(iters[1::]))
def test_call(div,num):
	cmd="adb shell input  keyevent 3"
	os.system(cmd)	
	cmd1 ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num # call start 
	rc = os.system(cmd1)
	print " CALL CONNECTING ......... To ",num
	time.sleep(10)
	cmd2 = "adb shell input  keyevent 6" # Call end 
	os.system(cmd2)
	os.system(cmd)
	os.system("adb kill-server")
	return rc
def iter_status(iteration,div,num):
	collect_logs()
	print "This program will execute "+str(iteration)+" Iterations"	
	for i in range(iteration):
		call= test_call(div,num)
		if call == 0:
			print "Test passed"
		else:
			print "Test Failed"
		
div = device.main()	
print div,"conncected device"
num=number()
iteration=iterations()
iter_status(iteration,div,num)
		
