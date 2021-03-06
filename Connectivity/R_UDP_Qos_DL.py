import re,os,subprocess,time
from subprocess import call,Popen,PIPE

def dev_id_and_ip():
#Getting adb devices
	global SAP_ID
	global SAP_IP
	global GO_ID
	global GO_IP
	global adb_dev
	global dev_ip
	adb_dev=[]
	dev_ip={}	
	cmd = "adb devices"
	os.system(cmd)
	adb_output = Popen(cmd, shell = True,stderr = PIPE,stdout = PIPE)
	out,err = adb_output.communicate()
	data = re.findall( r'([a-zA-Z]+[0-9]+[a-zA-Z0-9]+)|([0-9]+[a-zA-Z]+[0-9a-zA-Z]+)',out,re.M )
	for i in data:
		for j in i:
			if j:
				adb_dev.append(j)

	#print adb_dev,"\n"

	
	for i in adb_dev:
		cmd= "adb -s "+i+" shell netcfg | grep wlan0"
	#Getting ip addresses
		adb_ip = Popen(cmd, shell = True,stderr = PIPE,stdout = PIPE)
		out_ip,err_ip = adb_ip.communicate()
		ip_data= re.findall( r'[0-9]+(?:\.[0-9]+){3}', out_ip)
		for j in ip_data:
			ip=j	
			dev_ip[i]=ip
	print "\nDevices and IP addresses : ",dev_ip
	#SAP and GO details	
	for i in dev_ip.keys():
		if dev_ip[i] == "192.168.43.1":
			SAP_ID=i
			SAP_IP="192.168.43.1"
		elif dev_ip[i] == "192.168.49.1" :
			GO_ID=i
			GO_IP="192.168.49.1"
		else:
			pass
		
	#Getting ip address of PC
	global sys_ip
	cmd = "hostname -I"
	adb_output = Popen(cmd, shell = True,stderr = PIPE,stdout = PIPE)
	out,err = adb_output.communicate()
	sys_ip = out.strip()
	print sys_ip


def UDP_Qos_DL():
	global SAP_ID
	global SAP_IP
	global GO_ID
	global GO_IP
	global adb_dev
	global dev_ip
	global sys_ip
	for dev in adb_dev:
		STA_ID=dev
		STA_IP=dev_ip[dev]
		Server_IP=sys_ip
		Band_width="30M"
		Time_limit="300" #seconds		
		
		DL_server_cmd1 = " gnome-terminal -e 'adb -s "+STA_ID+" shell iperf -s -i 1 -u -w 65K -p 5000 ' "
		DL_server_cmd2 = " gnome-terminal -e 'adb -s "+STA_ID+" shell iperf -s -i 1 -u -w 65K -p 5001 ' "
		DL_server_cmd3 = " gnome-terminal -e 'adb -s "+STA_ID+" shell iperf -s -i 1 -u -w 65K -p 5002 ' "
		DL_server_cmd4 = " gnome-terminal -e 'adb -s "+STA_ID+" shell iperf -s -i 1 -u -w 65K -p 5003 ' "
		
		DL_client_cmd1 = " gnome-terminal -e 'iperf -c "+STA_IP+" -i 1 -u -w 14.5K -b 60M -t "+Time_limit+" -S 0x00 -p 5000 '"
		DL_client_cmd2 = " gnome-terminal -e 'iperf -c "+STA_IP+" -i 1 -u -w 14.5K -b 60M -t "+Time_limit+" -S 0x20 -p 5001 '"
		DL_client_cmd3 = " gnome-terminal -e 'iperf -c "+STA_IP+" -i 1 -u -w 14.5K -b 60M -t "+Time_limit+" -S 0xa0 -p 5002 '"
		DL_client_cmd4 = " gnome-terminal -e 'iperf -c "+STA_IP+" -i 1 -u -w 14.5K -b 60M -t "+Time_limit+" -S 0xe0 -p 5003 '"
				
		os.system(DL_server_cmd1)
		os.system(DL_server_cmd2)
		os.system(DL_server_cmd3)
		os.system(DL_server_cmd4)
		os.system(DL_client_cmd1)
		os.system(DL_client_cmd2)
		os.system(DL_client_cmd3)
		os.system(DL_client_cmd4)
		time.sleep(3)
dev_id_and_ip()
UDP_Qos_DL()






