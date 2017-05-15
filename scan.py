from os import walk, path

# scan()
# Input: String containing a directory path
# Output: List containing the file paths of all files found in the
# given directory path, including file in subdirectories.
#
# find_duplicates()
# Input: List containing file paths, Corresponding list containing
#        hashes of the files.
# Output: List containg lists of duplicate files

def scan(root_dir):

    file_paths = []

    for dir_name, sub_dir_list, files in walk(root_dir):

        for file_name in files:

            file_paths.append(dir_name
                             + '/'
                             + file_name
                             )

    return file_paths

def find_duplicates(file_list, file_hashes):
    
    scanned = []
    duplicates = []
    
    for pos_i, item_i in enumerate(file_list):
        
		# Check that the item has not already been
		# added to a duplicate list
		
        already_scanned = False
        for x in scanned:
            if item_i == x:
                already_scanned = True
        if already_scanned:
            continue
        else:
            scanned.append(item_i)
        
        current_dup = [item_i]
            
        for pos_j, item_j in enumerate(file_list):
            
			# Check we aren't comparing the same
			# file with itself
            if pos_i == pos_j:
                continue
            
            if file_hashes[pos_i] == file_hashes[pos_j]:
                current_dup.append(item_j)
                scanned.append(item_j)
        
		# If no duplicates for the current file were
		# found then current_dup will only contain 
		# one item
        if len(current_dup) > 1:
            
            duplicates.append(current_dup)
            
    return duplicates
        