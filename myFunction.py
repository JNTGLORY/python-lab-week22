def hello():
    print("hello Jane")
    print("how are you?")
    print("what God cannot do does not exist")

def hello1(name):
    print(f"hello {name}")
    print("how are you?")
    print("what God cannot do does not exist")
    
hello1('abena')

def Command(cmd): 
    import os
    os.system(cmd)

Command('ls')    