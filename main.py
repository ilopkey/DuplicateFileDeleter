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

for list_pos, dup_list in enumerate(file_dup):

    print 'Duplicate Set %i: ' % (list_pos+1)
    
    for path_pos, dup_file_path in enumerate(dup_list):
        
        print '%i: %s' % (path_pos+1, dup_file_path)

		
# TO ADD: A way to specify which file from a set of
#         duplicates the user wants to keep, default
#         will be the first in the list
#
#         Have the program delete the duplicate files