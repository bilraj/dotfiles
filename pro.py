import sys

class Searcher:
	def search(self, in_word, frequency, list_of_files):
		# Variable for list
		found_files = []
		
		count = 0
		for p in list_of_files:
			f = open(p).read()

			# For each file, loop through words and count
			for word in f.split():
				if in_word in word:
					count += 1

			# print if occurs at least as many times
			if count >= frequency:
				# Add file to list
				found_files.append(p)

			count = 0
	

#if __name__ == "__main__":
#	main()

