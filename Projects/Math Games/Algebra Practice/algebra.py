import random

def generate_one_step_problem():
    a = random.randint(-20, 20)
    b = random.randint(-20, 20)

    opt = random.choice(['+', '-'])
    
    if opt == '+': return f"x {opt} {b} = {a + b}", a
    else: return f"x {opt} {b} = {a - b}", a
    

def generate_two_step_problem():
    a = random.randint(-10, 10)
    b = random.randint(1, 10) 
    c = random.randint(-10, 10)
    
    if random.choice([True, False]): return f"{a}x + {b} = {a*c + b}", c
    else: return f"x/{b} + {c} = {a + c}", a * b
    

print("Welcome to the Algebra Practice Game!")

score = 0

for i in range(10):
    if random.choice([True, False]): problem, solution = generate_one_step_problem()
    else: problem, solution = generate_two_step_problem()
    
    print(f"Problem {i + 1}: {problem}")

    try: user_answer = int(input("Your answer: ").strip())
    except ValueError:
        print("Invalid Input.")
        continue
    
    if user_answer == solution:
        print("Correct!\n")
        score += 1
    else: print(f"Incorrect. The correct answer was {solution}.\n")

print(f"Game Over! Your final score: {score}/10")
