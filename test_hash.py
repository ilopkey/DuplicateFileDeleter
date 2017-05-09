import unittest
import os
import shutil

from hash import hash, hash_list

class HashTestCase(unittest.TestCase):

    test_names = ['a', 'b', 'c', 'd', 'e', 'f']
    test_type = '.txt'
    test_folder = 'tmp'
    
    text_unique = 'WOW'
    text_duplicate = 'Hello'
    text_triplicate = 'Hello World!'
    
    current_dir = os.getcwd()
    
    def create_file_paths(self):
    
        file_path = []
    
        for name in self.test_names:

            file_path.append( self.current_dir
                            + '/'
                            + self.test_folder
                            + '/' 
                            + name 
                            + self.test_type
                            )

        return file_path


    def create_test_dir(self):
 
        os.mkdir(self.test_folder)

        count = 1

        file_paths = self.create_file_paths()

        for path in file_paths:

            with open(path, 'w') as file:

                if count % 2 == 0:
                    file.write(self.text_triplicate)
                elif count == 1:
                    file.write(self.text_unique)
                else:
                    file.write(self.text_duplicate)

            count = count + 1

    def delete_test_dir(self):

        shutil.rmtree(self.current_dir + '/' + self.test_folder)

    def test_hash(self):
        
        self.create_test_dir()
        test_file_paths = self.create_file_paths()
        
        example_hash_a = hash(test_file_paths[0])
        self.assertEqual( hash(test_file_paths[0]), example_hash_a)
        
        example_hash_b = hash(test_file_paths[1])
        self.assertFalse(example_hash_a == example_hash_b)
        
        example_hash_c = hash(test_file_paths[3])
        self.assertEqual(example_hash_b, example_hash_c)
        
        self.delete_test_dir()
        
    def test_hash_list(self):
    
        self.create_test_dir()
        test_file_paths = self.create_file_paths()
        
        test_hash_list_a = hash_list(test_file_paths)
        test_hash_list_b = hash_list(test_file_paths)
        
        self.assertEqual(test_hash_list_a, test_hash_list_b)
        
        self.delete_test_dir()


if __name__=='__main__':
    unittest.main()