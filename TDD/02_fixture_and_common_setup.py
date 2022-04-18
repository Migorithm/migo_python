"""
We want our test to verify the follwing:

- If I add a new key-value pair to the state, it is recorded correctly in the state file.
- If I alter the value of an existing key, that updated value is written to the state file.
- If the state is not changed, the state file's content stays the same.

For each test, we want the state file to be in a known starting state. 
Afterwards, we want to remove that file, so we don't leave garbage files on the file system.
"""

import os
import unittest
import shutil
import tempfile
from statefile import State

INITIAL_STATE='{"foo":42,"bar":17}'

class TestState(unittest.TestCase):
    def setUp(self):
        self.testdir = tempfile.mkdtemp()      #1 
        self.state_file_path = os.path.join(
            self.testdir,"statefile.json"
        )
        with open(self.state_file_path, "w") as outfile:
            outfile.write(INITIAL_STATE)

        self.state = State(self.state_file_path)

    def tearDown(self): #2
        shutil.rmtree(self.testdir) #2 recursively delete a directory tree

    def test_change_value(self):
        self.state.data["foo"] = 21
        self.state.close()
        reloaded_statefile = State(self.state_file_path)
        self.assertEqual(21, reloaded_statefile.data["foo"])
    
    def test_remove_value(self):
        del self.state.data["bar"]
        self.state.close()
        reloaded_statefile = State(self.state_file_path)
        self.assertNotIn("bar", reloaded_statefile.data)

    def test_no_change(self):
        self.state.close()
        with open(self.state_file_path) as handle:
            checked_content = handle.read()
        self.assertEqual(checked_content, INITIAL_STATE)




"""
#1 In setUp, we create a temporary directory using tempfile.mkdtemp()

#2 We also want to clean up the temporary files; otherwise they will accumulate over time. The tearDown method will run after each
tech_* method completes EVEN IF some of its assertions fail.

The generic term for this kind of pre-test preparation is called a test fixture. 

A test fixture is whatever needs to be done before a test can properly run. 

A test fixture can be a mock database; a set of files in a known state; some kind of network connection; or starting a server process.


"""