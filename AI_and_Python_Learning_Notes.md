# Introduction to AI & Python — Learning Material

## 1. Basics of Artificial Intelligence

**Artificial Intelligence (AI)** is a field of computer science concerned with building computer systems that perform tasks commonly associated with human intelligence, such as recognizing patterns, understanding language, learning, reasoning, and making decisions.

AI does not mean a computer thinks exactly like a human. An AI system is designed to perform particular tasks using rules, data, algorithms, or models. Not every AI system learns from data; some use explicitly written rules or search procedures.

### Important terms
- **Data:** Facts or information that a computer system can process.
- **Algorithm:** A step-by-step procedure for solving a problem.
- **Model:** A computational system that produces an output from an input. In ML, a model is learned from training data.
- **Training:** Adjusting a machine-learning model using examples.
- **Prediction / inference:** Using a trained model to produce an output for new input.

### A typical AI workflow
1. Collect relevant data or define rules.
2. Prepare the input.
3. Process it using an algorithm or model.
4. Produce an output, recommendation, classification, or decision.
5. Evaluate the result and improve the system when necessary.

## 2. Basics of Machine Learning

**Machine Learning (ML)** is a subfield of AI. It develops methods that allow computers to learn patterns from data and use those patterns to make predictions or decisions, rather than requiring a programmer to write every decision rule manually.

### Example: spam email detection
1. Collect emails labelled `spam` or `not spam`.
2. Provide these examples to a learning algorithm.
3. The algorithm learns patterns associated with each category.
4. Use the trained model to classify a new email.
5. Check performance and improve the data or model when needed.

### Main types of ML
- **Supervised learning:** Learns from labelled data. Examples: spam classification and house-price prediction.
- **Unsupervised learning:** Finds patterns in data without supplied target labels. Example: grouping customers by purchasing behaviour.
- **Reinforcement learning:** An agent learns by interacting with an environment and receiving rewards or penalties. Example: an agent learning to play a game.

## 3. Difference between AI, ML, and Deep Learning

| Aspect | AI | ML | Deep Learning |
|---|---|---|---|
| Meaning | Broad field of intelligent systems | Part of AI that learns patterns from data | Part of ML using multi-layer neural networks |
| Scope | Broadest | Subfield of AI | Subfield of ML |
| Techniques | Rules, search, reasoning, planning, learning | Algorithms that learn from examples | Neural networks with multiple layers |
| Example | Rule-based game-playing system | Email spam classifier | Neural network for image recognition |

**Relationship:** Deep Learning (DL) is part of ML, and ML is part of AI.

```text
Artificial Intelligence
└── Machine Learning
    └── Deep Learning
```

## 4. Real-world applications of AI

1. **Healthcare:** Assisting medical-image analysis and clinical workflows. Outputs require professional oversight.
2. **Education:** Adaptive learning, personalized practice recommendations, and learning assistants.
3. **Finance:** Detecting unusual transactions, supporting risk analysis, and customer-service automation.
4. **Transportation:** Traffic prediction, route planning, and driver-assistance features.
5. **Retail and e-commerce:** Product recommendations, demand forecasting, and chatbots.
6. **Agriculture:** Crop monitoring, possible plant-disease identification, and irrigation support.
7. **Entertainment:** Recommending music, films, and videos.
8. **Cybersecurity:** Identifying unusual network behaviour and potential threats.

### Responsible AI
AI systems can make errors and may reproduce biases in their data. Responsible use includes checking accuracy, protecting personal information, securing systems, explaining limitations, and maintaining human oversight for important decisions.

## 5. Installing Python

1. Visit https://www.python.org/downloads/.
2. Download a Python 3 version for your operating system.
3. On Windows, select **Add Python to PATH** in the installer.
4. Complete installation and open Command Prompt or Terminal.
5. Verify the installation:

```bash
python --version
```

On some Windows installations, use `py --version`.

### First Python program
Create `hello.py`:

```python
print("Hello, AI and Python!")
```

Run it with `python hello.py`. Expected output: `Hello, AI and Python!`

You can use IDLE, Visual Studio Code, or another Python editor.

## 6. Python programming fundamentals

### 6.1 Variables
A variable is a named reference used to store a value.

```python
student_name = "Subhangi"
age = 20
cgpa = 9.4

print(student_name)
print(age)
print(cgpa)
```

Use meaningful names. Python is case-sensitive: `age` and `Age` are different.

### 6.2 Common data types

| Type | Meaning | Example |
|---|---|---|
| `int` | Whole number | `25` |
| `float` | Decimal number | `9.4` |
| `str` | Text | `"Python"` |
| `bool` | Boolean value | `True` or `False` |
| `list` | Ordered, mutable collection | `[10, 20, 30]` |

Use `type(value)` to check a value's data type.

### 6.3 Input and output
- `print()` displays information.
- `input()` accepts text typed by the user and returns a string.
- Convert input using `int()` or `float()` when a number is required.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello,", name)
print("Next year you will be", age + 1)
```

### 6.4 Conditional statements
Conditions allow a program to choose which block of code to execute.

```python
marks = 78

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Needs improvement")
```

`if` checks the first condition, `elif` checks another condition, and `else` runs if earlier conditions are false. Indentation matters in Python.

### 6.5 Loops
Loops repeat instructions.

**For loop:** iterates over a sequence or range.

```python
for number in range(1, 6):
    print(number)
```

**While loop:** repeats while its condition remains true.

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

Update the condition variable in a `while` loop so it eventually stops.

### 6.6 Functions
A function is a reusable block of code. It can receive inputs called parameters and return a result.

```python
def add(first_number, second_number):
    return first_number + second_number

answer = add(5, 3)
print(answer)
```

Functions reduce repeated code, organize programs, and make testing easier.

### 6.7 Lists
A list stores multiple items in one variable. Lists are ordered and mutable. Indexing starts at zero.

```python
subjects = ["Python", "Mathematics", "AI"]
print(subjects[0])

subjects.append("ML")
subjects.remove("AI")
print(subjects)
```

Useful operations:
- `append(item)` adds an item at the end.
- `remove(item)` removes the first matching item.
- `len(list_name)` returns the number of items.
- `sort()` sorts the list in place.

## 7. Beginner-friendly Python programs

The repository includes:
1. Variables and data types — collect and display user details.
2. Conditions and loops — check a number and print its multiplication table.
3. Functions — create greeting and addition functions.
4. Lists — add, display, count, and sort subjects.
5. Student grade calculator — calculate average marks and assign a simple grade.
6. Simple calculator — perform arithmetic using a function.

Run each program, try different inputs, and read the code to understand how it works.

## 8. Key takeaways
- AI is the broad field of building systems that perform tasks associated with intelligence.
- ML is a subfield of AI that learns patterns from data.
- DL is a subfield of ML that uses multi-layer neural networks.
- AI is used in healthcare, education, finance, transport, retail, agriculture, entertainment, and cybersecurity.
- Variables store values; conditions make decisions; loops repeat tasks; functions organize reusable logic; lists store collections.

## 9. Self-assessment
1. What is Artificial Intelligence?
2. What is Machine Learning, and how is it related to AI?
3. What is Deep Learning?
4. Explain the relationship between AI, ML, and DL.
5. Give four real-world applications of AI.
6. What is the difference between a `for` loop and a `while` loop?
7. Why are functions useful?
8. What is a list? Name three list operations.
9. What is the purpose of `input()` and `print()`?
10. Why should AI systems be tested and monitored?

## 10. Learning progress log
After each session, record the date, topics studied, programs completed, what you understood, errors or challenges, how you solved them, and what you will practise next.
