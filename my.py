import datetime


class WorkTime:
    def __init__(self, path, method):
        self.path = path
        self.method = method
    
    def __enter__(self): 
        self.file = open(self.path)
        self.start_time = datetime.datetime.now()
        return self.file, self.start_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_time = datetime.datetime.now()
        self.file.close()
        print(f'Время работы кода {self.stop_time - self.start_time}')

with WorkTime('mycode.py', 'r') as code:
    import mycode
