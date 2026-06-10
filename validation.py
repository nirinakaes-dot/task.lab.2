from datetime import datetime

def validate_task_title(title):
    if not title:
        raise ValueError('Title cannot be empty')
    if not isinstance(title,str):
        raise ValueError('Task must be a string')
    if len (title)<3:
        return False ('Task must be more than 3 characters long')
def validate_task_description(description):
    if not description:
        raise ValueError('Description cannot be empty')
    
def validate_due_date(due_date):
    if not due_date:
        raise ValueError('Enter a valid date')
    

    