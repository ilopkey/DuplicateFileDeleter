import unittest
import os
import shutil

from scan import scan, find_duplicates

class self(unittest.TestCase):

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

    def test_scan(self):

        self.create_test_dir()

        directory = (
                    self.current_dir 
                    + '/'
                    + self.test_folder
                    )

        test_file_paths = []

        for name in self.test_names:

            test_file_paths.append(directory 
                                    + '/'
                                    + name
                                    + self.test_type
                                    )

        self.assertEqual( 
                        sorted( scan(self.test_folder) ),
                        sorted( test_file_paths )
                        )

        fake_dir = 'not_a_dir'

        self.assertEqual(
                        scan(fake_dir),
                        []
                        )

        self.delete_test_dir()


    def test_find_duplicates(self):
    
        mock_hashes = ['1', '2', '1', '3', '1', '3']

        mock_files = self.test_names

        expected_duplicates = [ ['a', 'c', 'e'], 
                                ['d', 'f']
                              ]

        self.assertEqual( find_duplicates(mock_files, mock_hashes),
                          expected_duplicates )
                          
        self.assertEqual( find_duplicates([], []),
                          [])

        self.assertEqual( find_duplicates(['a'], [1]),
                          [])


if __name__=='__main__':
    unittest.main()
