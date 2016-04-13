import sys
import subprocess 

class Compiler:

	function_defs = ""

	def __init__(self, file_to_compile):
		try:
			p = subprocess.check_call([r"/usr/bin/g++", "-Wall", "-o", "test", file_to_compile], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		except subprocess.CalledProcessError as grepx:
			print("Compilation error in " + file_to_compile)
			p.terminate()
	
	def compile_tests(self, tests):
		for file in tests:
			s = file.split(".")
			o = s[0]
		try:
			p = subprocess.Popen([r"/usr/bin/g++", "-Wall", "-o", o, file + function_defs], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		except subprocess.CalledProcessError as grepx:
			print("Compilation error in " + file)
	def def_file(self, name):
		self.function_defs = name
		print("Name is: " + self.function_defs)

	def run_tests(self, tests):
		count = 0
		success = 0
		for file in tests:
			try:
				s = file.split(".")
				ex = s[0]
				p = subprocess.Popen(["./" + ex], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				p.communicate()
				success += 1
				count += 1
				print("Success")
				
			except subprocess.CalledProcessError as grepx:
				print("Test failed")
				count += 1
				

