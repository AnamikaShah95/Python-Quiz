questions = [
    ["Which function is used to display output in Python?", "echo()", "print()", "display()", "show()", 2],
    ["What is the correct way to start a comment in Python?", "#", "//", "/*", "--", 1],
    ["Which of the following is NOT a Python data type?", "int", "float", "real", "str", 3],
    ["What is the output of len('Python')?", "5", "6", "7", "Error", 2],
    ["Which keyword is used to create a loop in Python?", "repeat", "loop", "for", "iterate", 3],
    ["Which of the following is used to import a module in Python?", "include", "import", "require", "using", 2],
    ["What is the output of bool(0)?", "True", "False", "0", "Error", 2],
    ["Which method is used to add an element to a list?", "append()", "add()", "insert()", "push()", 1],
    ["What is the output of 'Python'.lower()?", "PYTHON", "python", "Python", "error", 2],
    ["Which of the following is used to handle exceptions?", "catch-finally", "try-except", "error-check", "if-else", 2],
    ["Which of the following creates a generator in Python?", "[]", "{}", "()", "yield", 4],
    ["What is the output of sum([i for i in range(5)])?", "10", "15", "5", "Error", 1],
    ["Which of the following is true about Python dictionaries?", "They are ordered", "They allow duplicate keys", "They store key-value pairs", "They are immutable", 3],
    ["Which of the following is used to define a class?", "function", "class", "def", "object", 2],
    ["What is the output of type((1,))?", "list", "tuple", "int", "dict", 2]
]

points = [1,1,1,1,1,2,2,2,2,2,4,4,4,4,4]
score = 0
i = 0

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    
    # Convert input to integer
    a = int(input("\nFor answering enter :\n 1 for option a \n 2 for option b \n 3 for option c \n 4 for option d\n\nEnter your answer (1-4):   "))
    
    if question[5] == a:
        print("Correct Answer")
        score += points[i]
    else:
        print(f"Incorrect, the correct answer was option {question[5]}")
        print("Better luck next time!")
        break
    
    print(f"You have {score} points\n")
    i += 1
