from functions import Atom
from functions import List
from functions import cons

operators = ['+','-','*','/']
list_of_commands = ['atom','quote','car','cdr','eq','cond','lambda','label','defunc']

def evaluator(command):
    if '(' not in command and ')' not in command:
        Atom.Unit(command)
    elif 'cons' in command:
        cons.Cons(command)

        # List.List(command)

print("Welcome to a lisp interpreter.\n")
command = ""
while command != "exit" and command != "quit":
    command = input('>> ')
    evaluator(command)

