import os
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))
print(os.path.join(os.path.dirname(os.path.abspath(__file__))),'/static/')
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))