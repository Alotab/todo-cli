import datetime 



class Todo:
    def __init__(self, task, category, date_added=None, 
                 date_complated=None, status=None, position=None):
        
        self.task = task
        self.category= category
        self.date_added = date_added if date_added is not None else datetime.datetime.now().isoformat()
        self.date_complated = date_complated if date_complated is not None else None
        self.status = status if status is not None else 1 # 1 = open, 2  = completed
        self.position = position if position is not None else None


    
    def __repr__(self) -> str:
        return f"({self.task}, {self.category},{self.date_added}, {self.date_complated}, {self.status}, {self.position})"
    