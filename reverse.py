class Reverse:
    def __init__(self, s=""):
        self.s = s

    def set_string(self, input_str):
        self.s = input_str

    def get_reversed(self):
        return self.s[::-1]

string_obj = Reverse() 
user_input = input("Enter a word: ")
string_obj.set_string(user_input)
print(f"Reversed string: {string_obj.get_reversed()}")