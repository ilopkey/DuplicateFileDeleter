import hashlib

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