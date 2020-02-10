import datetime
import mycode

class WorkTime:
    def __init__(self, path, method):
        self.path = path
        self.method = method
    
    def __enter__(self): 
        self.file = open(self.path)
        start_time = datetime.datetime.now()
        print(start_time)
        return self.file, start_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        stop_time = datetime.datetime.now()
        self.file.close()
        print(stop_time)
        print(stop_time - start_time)

with WorkTime('mycode.py', 'r') as code:
    print('gkuukj')
