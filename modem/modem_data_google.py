import os,time,datetime,csv,random
import device
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('data_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	os.chdir(mydir)
	cmdr='adb logcat -b radio  > data_log'+'&'
	os.system(cmdr)

def data_on(div):
	cmd= "adb -s "+div+" shell svc data enable"
	try:
		rc=os.system(cmd)	
		print "data enabled"
	except:
		print "sorry"	
	time.sleep(10)
	return rc
def iterations():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	iters=your_list[2]
	return int(random.choice(iters[1::]))

def open_browse():
	cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d "+address
	rc=os.system(cmd)
	print "google opened"
	time.sleep(20)
	return rc
def not_browse():
	cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d "+address
	rc=os.system(cmd)
	print "google notopened"
	time.sleep(10)
	return rc

def data_off():
	cmd= "adb -s "+div+" shell svc data disable"
	rc=os.system(cmd)
	print "data disabled"
	time.sleep(10)
	return rc

def iter_status(iterations,div,address):
	collect_logs()
	for i in range(iterations):
		on=data_on(div)
		browse=open_browse()
		off=data_off()
		browse1= not_browse()

div =device.main()
print div," device Connected "
address="http://google.com"
iterations=iterations()
iter_status(iterations,div,address)


