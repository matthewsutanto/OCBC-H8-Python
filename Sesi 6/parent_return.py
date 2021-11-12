def parent(num):
    def first_child():
        print("Hi this is first child")
        
    def second_child():
        print("Hi this is second child")
        
    if num==1:
        return first_child()
    else:
        return second_child()
        