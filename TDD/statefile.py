class State:
    def __init__(self,state_file_path:str):
        "Load the stored state data, and save it in self.data"
        self.data={}
    
    def close(self):
        "Handle any changes on application exit"