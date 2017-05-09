from scan import scan, find_duplicates
from hash import hash_list

directory = raw_input('Please enter the directory to scan: ')

file_list = scan(directory)

file_list_hashes = hash_list(file_list)

file_dup = find_duplicates(file_list, file_list_hashes)

print file_dup