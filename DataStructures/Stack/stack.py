from DataStructures.List import single_linked_list as lt
def new_stack():
    stacky = lt.new_list()
    return stacky
def push(my_stack,element):
    my_stack = lt.add_first(my_stack,element)
    return my_stack