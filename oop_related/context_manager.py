# Using these magic methods (__enter__, __exit__)
# allows you to implement objects which can be used easily 
# with the "with" statement.

class Open_File():
    def __init__(self,filename,mode):
        self.filename = filename 
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self,exec_type,exc_val,traceback):
        self.file.close()

#with Open_File("sample.txt",'w') as f:
#    f.write("Testing")




#Or you can implement pretty much the same functionality with this:
from contextlib import contextmanager
@contextmanager
def open_file(file,mode):
    #Doing this will ensure even if we ran into an error, 
    # the tearDown code will get run. 
    try:
        f = open(file,mode)
        yield f
    finally:
        f.close()

#with open_file("sample2.txt","w") as f:
 #   f.write("Lorem ipsum dolor sit amet,")

#print(f.closed)


# But 'open' is already a context manager within python. So now, take a look 
# at a practical example.

import os
@contextmanager
def change_dir(destination):
    try:
        if not os.path.exists(destination):
            os.mkdir(destination)
        cwd = os.getcwd()
        os.chdir(destination)
        yield      # It's okay not to put object 
                   # All the commands will be executed within this context.         
    finally:
        #Change directory back to original
        os.chdir(cwd)
        print(os.getcwd())

with change_dir("/Users/we/Downloads/"):
    print(os.listdir())