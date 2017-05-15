import hashlib

# hash()
# Input: string containing a file path
# Output: string containing a md5 hash of the contents
#         of the file pointed to by the file path

# hash_list()
# Input: list of strings containing file paths
# Output: corresponding list of hashes made
#         by looping through the list and applying
#         the hash() function to each file path

def hash(file_path):
    
	hasher = hashlib.md5()
	
	with open(file_path, 'rb') as file:
	    
		buf = file.read()
		hasher.update(buf)
	
	return hasher.hexdigest()
	
def hash_list(file_paths):
    
	file_hash = []
	
	for i in range( len(file_paths) ):
	    
		file_hash.append( hash(file_paths[i]) )
		
	return file_hash