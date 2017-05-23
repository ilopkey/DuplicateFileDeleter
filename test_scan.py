import unittest
import os
import shutil

from scan import scan, find_duplicates

class ScanTestCase(unittest.TestCase):

    test_names = ['a', 'b', 'c', 'd', 'e', 'f']
    test_type = '.txt'
    test_folder = 'tmp'
    
    text_unique = 'WOW'
    text_duplicate = 'Hello'
    text_triplicate = 'Hello World!'
    
    current_dir = os.getcwd()
    
    # generates a list of file paths for the files used for testing
    
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

    # create a directory for testing and populate it
    # with 6 txt files containing duplicate files

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

    # delete the test directory and all files inside it
            
    def delete_test_dir(self):

        shutil.rmtree(self.current_dir + '/' + self.test_folder)

    # tests for the scan() function
        
    def test_scan(self):

        # create the test directory and get the file paths
        self.create_test_dir()
        test_file_paths = self.create_file_paths
        
        # make sure the scan function returns the same
        # file paths as the ones used to create the 
        # test folder
        
        self.assertEqual( 
                        sorted( scan(self.test_folder) ),
                        sorted( test_file_paths )
                        )
        
        # make sure the scan function returns an empty list
        # when given a directory that doesn't exist
        
        fake_dir = 'not_a_dir'

        self.assertEqual(
                        scan(fake_dir),
                        []
                        )
                        
        # delete the test directory
        self.delete_test_dir()


    def test_find_duplicates(self):
    
        # because the find duplicates function doesn't need 
        # actual hashes to work, create simple mock hashes
        # for testing and use the test file names for mock files
        mock_hashes = ['1', '2', '1', '3', '1', '3']
        mock_files = self.test_names

        # with the mock_hashes and mock_files these are the
        # expected sets of duplicates
        expected_duplicates = [ ['a', 'c', 'e'], 
                                ['d', 'f']
                              ]
        
        # make sure find_duplicates returns the expected duplicates
        self.assertEqual( find_duplicates(mock_files, mock_hashes),
                          expected_duplicates )
        
        # make sure find_duplicates returns returns an empty list
        # when the inputs are empty
        self.assertEqual( find_duplicates([], []),
                          [])

        # make sure find_duplicates returns an empty list when given
        # a single item in the input lists
        self.assertEqual( find_duplicates(['a'], [1]),
                          [])

        # make sure find_duplicates returns an empty list when given
        # lists containing no duplicate hashes

        self.assertEqual( find_duplicates(['a', 'b', 'c'],
                                          [1, 2, 3] ) )
        
if __name__=='__main__':
    unittest.main()
