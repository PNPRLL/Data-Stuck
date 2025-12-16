class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
                    pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        if self.data == []:
            print("Underflow: Cannot pop data from an empty list")
            return None
        self.size -= 1
        return self.data.pop()

    def is_empty(self):
        if self.data == []:
            return True
        else:
            return False

    def get_stack_top(self):
            if self.data == []:
                print("Underflow: Cannot get stack top from an empty list")
                return None
            return self.data[-1]

    def get_size(self):
        return self.size

    def print_stack(self):
        print(self.data)


word = str(input())
def is_parentheses_matching():
    if word[0] == ")" or word[-1] == "(":
        