import os

test_names = ['a', 'b', 'c', 'd', 'e', 'f']
test_type = '.txt'
test_folder = 'tmp'

text_unique = 'WOW'
text_duplicate = 'Hello'
text_triplicate = 'Hello World!'

current_dir = os.getcwd()

def create_file_paths():

	file_path = []

	for name in test_names:

		file_path.append( current_dir
						+ '/'
						+ test_folder
						+ '/' 
						+ name 
						+ test_type
						)

	return file_path


def create_test_dir():

	os.mkdir(test_folder)

	count = 1

	file_paths = create_file_paths()

	for path in file_paths:

		with open(path, 'w') as file:

			if count % 2 == 0:
				file.write(text_triplicate)
			elif count == 1:
				file.write(text_unique)
			else:
				file.write(text_duplicate)

		count = count + 1
		
create_test_dir()