import random as rd

def get_random_int(min_value, max_value):
    """
    Args:
        min_value (int): lower limit of the range of allowed random integers (inclusive)
        max_value (int): upper limit of the range of allowed random integers (inclusive)

    Returns:
        int: random integer between min_value (inclusive) and max_value (inclusive)
    """
    return rd.randint(min_value, max_value)


def get_operator():
    """
    Returns:
        string: an operator (+, -, *) to connect two numbers within a math problem
    """
    return rd.choice(['+', '-', '*'])


def get_task_with_solution(first_number, second_number, operator):
    """
    Args:
        first_number (int): number in front of the operator in the math problem
        second_number (int): number following the operator in the math problem
        operator (string): an operator (+, -, *) that connects the two numbers within the math problem

    Returns:
        (string, int): tuple consisting of the problem statement as a format string and the exact result of the given math problem
    """
    problem_statement = f"{first_number} {operator} {second_number}"
    if operator == '+': 
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    else: 
        result = first_number * second_number

    return (problem_statement, result)

def math_quiz():
    # score_counter is used to count the number of correctly answered questions for a final print statement
    score_counter = 0
    total_number_of_questions = 10

    print("Welcome to the Math Quiz Game!\nYou will be presented with math problems, and you need to provide the correct answers.")

    # loop over all questions
    for i in range(total_number_of_questions):
        # generate random integer numbers and an operator to connect these numbers
        first_number = get_random_int(1, 10)
        second_number = get_random_int(1, 5)
        operator = get_operator()

        (task_problem, result) = get_task_with_solution(first_number, second_number, operator)
        print(f"\nQuestion: {task_problem}")
        
        repeat = True
        while repeat:
            # get user input
            user_answer = input("Your answer: ")
            try: 
                user_answer = int(user_answer)
            except ValueError:
                print('Your answer has to be a signed integer value!\nRetry!')
            else:
                repeat = False
        
        # compare user input with the actual result
        if user_answer == result:
            print("Correct! You earned a point.")
            score_counter += 1
        else:
            print(f"Wrong answer. The correct answer is {result}.")

    print(f"\nGame over! Your score is: {score_counter}/{total_number_of_questions}")

if __name__ == "__main__":
    math_quiz()
