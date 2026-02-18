from DataStructures.List import single_linked_list as lt
def new_stack():
    stacky = lt.new_list()
    return stacky
def push(my_stack,element):
    if my_stack["size"] == 0:
        my_stack = lt.add_first(my_stack,element)
    else:
        my_stack["last"] = my_stack["first"]
        my_stack = lt.add_first(my_stack,element)
    return my_stack
def pop(my_stack):
    if my_stack["size"] == 0:
        return 'EmptyStructureError: stack is empty'
    else:
        my_stack = lt.remove_first(my_stack)
        return my_stack
def is_empty(my_stack):
    if my_stack["size"] == 0:
        return True
    else:
        return False
    
    
def top(my_stack):
    if my_stack["size"] == 0:
        return 'EmptyStructureError: stack is empty'
    else:
        return my_stack["first"]["info"]
def size(my_stack):
    return my_stack["size"]
    
