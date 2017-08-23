import subprocess
cmd = "python run.py discover 1 >dm_test.log"
try:
	p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out,err = p.communicate()
	print (out,err)
except Exception:
	print("error")