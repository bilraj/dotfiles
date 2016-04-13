import sys

def main():
	# Read word
	word_to_compare = sys.argv[1]

	# Read int 
	num_of_occurrances = sys.argv[2]

	list_of_files = []

	# Read through all the files
	for arg in sys.argv:
		if arg == word_to_compare:
			continue
		elif arg == num_of_occurrances:
			continue

		# For the current file, loop through words 
		list_of_files.append(arg)

	# Remove first element
	list_of_files.pop(0)

	count = 0

	# Convert to int
	num_of_occurrances = int(num_of_occurrances)

	for p in list_of_files:
		f = file(p).read()

		# For each file, loop through words and count
		for word in f.split():
			if word_to_compare in word:
				count += 1

		# print if occurs at least as many times
		if count >= num_of_occurrances:
			print(p)

		count = 0

if __name__ == "__main__":
	main()

