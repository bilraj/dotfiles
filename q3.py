import sys
import subprocess 
import glob

try:
	p = subprocess.check_call([r"/usr/bin/g++", "-Wall", "-o", "test", file_to_compile], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

except subprocess.CalledProcessError as grepx:
	print("Compilation error in " + file_to_compile)
	p.terminate()

for file in glob.glob("test*.cpp"):
	s = file.split(".")
	o = s[0]
	try:
		p = subprocess.Popen([r"/usr/bin/g++", "-Wall", "-o", o, file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	except subprocess.CalledProcessError as grepx:
		print("Compilation error in " + file)
		p.terminate()

#for file in tests:
#	try:
#		s = file.split(".")
#		ex = s[0]
#		p = subprocess.Popen(["./" + ex], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#		p.communicate()
#		success += 1
#		count += 1
#		print("Test suceeded")
#		
#	except subprocess.CalledProcessError as grepx:
#		print("Test failed")
#		count += 1
				

