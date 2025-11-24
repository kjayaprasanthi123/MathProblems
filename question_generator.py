import random

# -------------------------
# MAIN ENTRY FUNCTION
# -------------------------

def generate_math_question():
    question_types = [
        generate_addition,
        generate_subtraction,
        generate_multiplication,
        generate_division,
        generate_percentage,
        generate_word_problem
    ]

    # Pick a random generator function
    generator = random.choice(question_types)
    return generator()


# ------------------------------
# SIMPLE MATH TYPES
# ------------------------------

def generate_addition():
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    return {
        "type": "addition",
        "question": f"What is {a} + {b}?",
        "variables": {"a": a, "b": b},
        "correct_answer": a + b
    }


def generate_subtraction():
    a = random.randint(50, 100)
    b = random.randint(1, 50)
    return {
        "type": "subtraction",
        "question": f"What is {a} - {b}?",
        "variables": {"a": a, "b": b},
        "correct_answer": a - b
    }


def generate_multiplication():
    a = random.randint(2, 20)
    b = random.randint(2, 20)
    return {
        "type": "multiplication",
        "question": f"What is {a} × {b}?",
        "variables": {"a": a, "b": b},
        "correct_answer": a * b
    }


def generate_division():
    b = random.randint(2, 10)
    a = b * random.randint(2, 10)  # ensures no decimals
    return {
        "type": "division",
        "question": f"What is {a} ÷ {b}?",
        "variables": {"a": a, "b": b},
        "correct_answer": a // b
    }


# ------------------------------
# PERCENTAGE QUESTION
# ------------------------------

def generate_percentage():
    a = random.randint(50, 500)
    percent = random.randint(5, 50)
    correct = (a * percent) // 100
    return {
        "type": "percentage",
        "question": f"What is {percent}% of {a}?",
        "variables": {"percent": percent, "a": a},
        "correct_answer": correct
    }


# ------------------------------
# SCENARIO WORD PROBLEMS
# ------------------------------

def generate_word_problem():
    templates = [
        {
            "scenario": "A nurse gives {x} ml of medicine to {y} patients. How much medicine is used?",
            "formula": lambda x, y: x * y
        },
        {
            "scenario": "A welder cuts {x} rods, each {y} cm long. What is the total length?",
            "formula": lambda x, y: x * y
        },
        {
            "scenario": "A carpenter buys {x} planks for {y} rupees each. What is the total cost?",
            "formula": lambda x, y: x * y
        }
    ]

    chosen = random.choice(templates)
    x = random.randint(1, 20)
    y = random.randint(5, 50)

    return {
        "type": "word_problem",
        "question": chosen["scenario"].format(x=x, y=y),
        "variables": {"x": x, "y": y},
        "correct_answer": chosen["formula"](x, y)
    }
