print("Welcome to the quiz game")

name = input("Enter your Name:\n")

print(name, "You have 4 questions to answer")

quiz_question = [
    {"question": "What is the capital of India", "Answer": "B"},
    {"question": "What is the capital of Sri Lanka", "Answer": "A"},
    {"question": "What is the capital of Bhutan", "Answer": "C"},
    {"question": "What is the capital of Myanmar", "Answer": "D"}
]

quiz_answer = [
    ["A.New York", "B.New Delhi", "C.London", "D.Chennai"],
    ["A.Colombo", "B.Chittagong", "C.Dhaka", "D.Mumbai"],
    ["A.New Delhi", "B.Islamabad", "C.Thimpu", "D.Paro"],
    ["A.Yangon", "B.Thimpu", "C.Islamabad", "D.Naypyidaw"]
]

score = 0

def answer(option, ans):
    if option == ans:
        return True
    else:
        return False

for question in range(len(quiz_question)):
    print("__________________________________________________")
    print("Question Number", question + 1)
    print(quiz_question[question]["question"])
    for i in quiz_answer[question]:
        print(i)
        
    option = input("Enter A/B/C/D: ").upper()

    ans = quiz_question[question]["Answer"]

    if answer(option, ans):
        print("Correct Answer!")
        score += 100
    else:
        print("Wrong Answer!")
    print(name,"your score is",score)


print(name, "your total score is:\n", score)
print(name,"your accuraccy is",int((score/(len(quiz_question)*100)*100)),"%")