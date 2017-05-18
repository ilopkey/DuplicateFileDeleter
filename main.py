from scan import scan, find_duplicates
from hash import hash_list

# Get data from the user, the directory to scan and if they
# want to specify file types

directory = raw_input('Please enter the directory to scan: ')

scan_range = raw_input('Please select from the following options:'
                       + '\n\t'
                       + '1. Scan all files in the directory'
                       + '\n\t'
                       + '2. Scan a specific file type'
                       + '\n\t'
                       + '3. Scan multiple specific file types'
                       + '\n\t'
                      )


# If the user wants to specify file type/s, get which types
# they want and add them to a list, file_types 

file_types = []
    
if scan_range == '2':

    file_types.append( raw_input('Please enter the file type now: ') )
    
elif scan_range == '3':
    
    print ('You will now be asked to enter your chosen file types'
		+ '\n'
        + 'Please enter them one at a time'
		+ '\n'
        + 'When you are finished type DONE to continue'
		+ '\n'
          )
    
    while True:
        user_input = raw_input('Please enter the file type now: ')
        if user_input == 'DONE':
            break
        else:
            file_types.append(user_input)

else:

    print 'No file type specified, scanning all file types'

# Get a list of file paths from the directory given by the user
# Then if file types were specfied go through raw_file_list
# and add any file_paths ending with the file types to file_list

raw_file_list = scan(directory)

if scan_range == '2' or scan_range == '3':
    file_list = []
    for file in raw_file_list:
        
        correct_type = False
        
        for type in file_types:
            if file.endswith(type):
                correct_type = True
                break
                
        if correct_type:
            file_list.append(file)
            
else:
    file_list = raw_file_list

# Create a list of hashes corresponding to file_list
# Then create a list containing lists of files that
# have duplicate hashes

file_list_hashes = hash_list(file_list)

file_dup = find_duplicates(file_list, file_list_hashes)

# Print out the sets of duplicates to the user

# Please note the +1 is used for user readability. This is 
# repeated several times in the program including -1 when 
# receiving data from the user.

for list_pos, dup_list in enumerate(file_dup):

    print 'Duplicate Set %i: ' % (list_pos+1)
    
    for path_pos, dup_file_path in enumerate(dup_list):
        
        print '%i: %s' % (path_pos+1, dup_file_path)

# Give the user different options for how they choose which
# duplicate to keep from each list
# 1: Use the first duplicate from each set
# 2: Let the user choose from each set
# 3: Let the user choose which sets they want to choose a duplicate to keep
#    then just use the first duplicate for the rest

print 'There are %i sets of duplicates' % len(file_dup)
print ('Options: '
        + '\n\t'
        + '1. Keep the first duplicate listed from each set.'
        + '\n\t'
	    + '2. Select from each set which duplicate you want to keep.'
        + '\n\t'
	    + '3. Select which sets you wish to choose which duplicate you keep.'
        + '\n\t'
	    + '   (Note any set you do not choose will only keep the first one)')

dup_selection_method = raw_input('Please enter your choice: ')

# Used to store files for deletion
file_del = []

# 1: Loop through file_dup, then loop through each list, then
#    add all files apart from the first to file_del

if dup_selection_method == '1':
	
	for dup_list in file_dup:
		
		for dup_pos, dup_item in enumerate(dup_list):
		
			if dup_pos == 0:
				continue
			file_del.append(dup_item)

# 2: Loop through file_dup, print out a list of duplicates then 
#    ask the user which duplicate they want to keep then add
#    the rest to file_dup

elif dup_selection_method == '2':
	
	for list_pos, dup_list in enumerate(file_dup):
		
		print 'Duplicate Set %i: ' % (list_pos+1)

		for path_pos, dup_file_path in enumerate(dup_list):
			
			print '%i: %s' % (path_pos+1, dup_file_path)
			
		while True:
			keep = input('Which duplicate do you wish to keep: ')
			if keep < len(dup_list) or keep > 1: 
				keep = keep - 1
				break
			else:
				print 'Position given not on list, try again'
		
		for dup_path in dup_list:
		
			if dup_path == dup_list[keep]:
				continue
			else:
				file_del.append(dup_path)

# 3: Get the number of a list from the user, print out the list
#    then get the number of the file the suer wants to keep, then
#    add the other files on the list to file_del
#    Repeat until the user is done, then use the first file of each
#    list as the file to keep

elif dup_selection_method == '3':
	
	print ('Enter the no. of the list to specify which'
		+ 'duplicate you want to keep'
		+ '\n'
		+ 'When you are done enter DONE to continue')
		
	# Track which lists of duplicates have been scanned
	lists_scanned = []
	
	while True:
		
		cur_list = raw_input('List No. : ')
		
		# Input Checks
		
		# Check if the user wants to stop
		if cur_list == 'DONE':
			break
		
		# Check the input is a number
		try:
			cur_list = int(cur_list)
		except ValueError:
			print 'Wrong Value given, enter either DONE or a number'
			continue
		
		# Check input is in the range of file_dup
		if cur_list > len(file_dup) or cur_list < 1:
			print 'There are %i lists of duplicates' % len(file_dup)
			continue
		
		# Check the list hasn't already been scanned
		scanned = False
		
		cur_list = cur_list - 1
		
		for i in lists_scanned:
			if i == cur_list:
				scanned = True
		if scanned == True:
			print 'A duplicate has already been chosen for this list.'
			continue
		
		
		# Print the list to the user
		
		for file_pos, file_item in enumerate(file_dup[cur_list]):
			
			print '%i: %s' % (file_pos+1, file_item)
		
		keep = 0
		
		while True:
			keep = input('Enter file no. to keep: ')
			
			if keep > len(file_dup[cur_list]) or keep < 1:
				print 'No. given is not on this list'
			else:
				break
				
		for file_pos, file_item in file_dup[cur_list]:
			if file_pos == keep:
				continue
			else:
				file_del.append(file_item)
				
		lists_scanned.append(cur_list)
		
# TO ADD: A way to specify which file from a set of
#         duplicates the user wants to keep, default
#         will be the first in the list
#
#         Have the program delete the duplicate files