# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

'''You need to master the following to complete this assignment:
    Creating and indexing dictionaries
    Writing functions and function arguments
    Using various operators.'''

# Add your code after this line

def greet(name, template="Hello, <name>!"):
    print(f"{template} {name}!")
    return f"{template}, {name}!"


greet("Sandy", "Whats up <name>")