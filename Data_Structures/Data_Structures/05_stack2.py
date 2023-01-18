class Stack:
    def __init__(self):
        self.itmes = []

    def push(self, val):
        self.itmes.append(val)
    
    def pop(self):
        try:
            return self.itmes.pop()
        except:
            return print("Stack is empty")

    def top(self):
        try:
            return self.itmes[-1]
        except:
            return print("Stack is empty")

    def __len__(self):
        return len(self.itmes)

    def isEmpty(self):
        return len(self) == 0

    
def is_valid_ps(test_string):

    S = Stack()

    for i in range(len(test_string)):
        if test_string[i] == '(':
            S.push('(')
        else:
            if len(test_string) == 0 or test_string[len(test_string) -1 ] == ')':
                return "NO"
            else:
                S.pop()

        if len(test_string) == 0:
            return "Yes"
        else:
            return "NO"