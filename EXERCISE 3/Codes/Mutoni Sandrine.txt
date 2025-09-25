Project 78
Stack Questions
1. Practical (Rwanda): UR pushes ["Note1", "Note2", "Note3"]. Undo 2. Which is left?
Code (Python):
# Initialize stack
stack = []

# Push elements
stack.append("Note1")
stack.append("Note2")
stack.append("Note3")

print("Stack after pushes:", stack)

# Undo 2 (pop twice)
stack.pop()
stack.pop()

print("Stack after undo 2:", stack)

Output (screenshot-style):
Stack after pushes: ['Note1', 'Note2', 'Note3']
Stack after undo 2: ['Note1']

2. Practical (Rwanda): In Irembo, push ["Upload File", "Fill Details", "Confirm"]. Undo 1. Which is left?
Code (Python):
# Initialize stack
stack = []

# Push elements
stack.append("Upload File")
stack.append("Fill Details")
stack.append("Confirm")

print("Stack after pushes:", stack)

# Undo 1 (pop once)
stack.pop()

print("Stack after undo 1:", stack)

Output (screenshot-style):
Stack after pushes: ['Upload File', 'Fill Details', 'Confirm']
Stack after undo 1: ['Upload File', 'Fill Details']

Challenge: Push ["1", "2", "3", "4"], pop 3, push "5". Which is top?
Algorithmic Steps:

Initialize an empty stack.

Push "1", then "2", then "3", then "4" onto the stack.

Pop 3 times from the stack (remove the last three pushed elements).

Push "5" onto the stack.

Check the top of the stack (the last pushed element).

Code & Explanation:
stack = []

# Step 2: Push "1", "2", "3", "4"
stack.append("1")    # Stack: ["1"]
stack.append("2")    # Stack: ["1", "2"]
stack.append("3")    # Stack: ["1", "2", "3"]
stack.append("4")    # Stack: ["1", "2", "3", "4"]

# Step 3: Pop 3 times
stack.pop()          # Removes "4", stack: ["1", "2", "3"]
stack.pop()          # Removes "3", stack: ["1", "2"]
stack.pop()          # Removes "2", stack: ["1"]

# Step 4: Push "5"
stack.append("5")    # Stack: ["1", "5"]

# Step 5: Top of the stack
top = stack[-1]
print("Top of the stack:", top)


Output:

Top of the stack: 5

Reflection: Why stack represents memory history?

A stack follows the Last In, First Out (LIFO) principle, meaning the most recent action is the first to be reversed or revisited. This makes stacks perfect for representing memory history or undo operations, where you want to backtrack or undo the latest changes first. For example, when you press "undo" in a text editor, the last change made is undone first — this mirrors the stack behavior exactly. Thus, stacks efficiently track and manage the order of past actions.

Queue Questions
1. Practical (Rwanda): At Nyabugogo, 12 buses queue. After 8 depart, who is front?
Code (Python):
from collections import deque

# Initialize queue with buses labeled 1 to 12
queue = deque(range(1, 13))  # buses 1 to 12

print("Initial queue:", list(queue))

# 8 buses depart (remove from front)
for _ in range(8):
    queue.popleft()

print("Queue after 8 depart:", list(queue))
print("Bus at front now:", queue[0])

Output:
Initial queue: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Queue after 8 depart: [9, 10, 11, 12]
Bus at front now: 9

2. Practical (Rwanda): At CHUK, 5 patients queue. Who is served second?
Code (Python):
from collections import deque

# Initialize queue with patients 1 to 5
queue = deque(range(1, 6))  # patients 1 to 5

print("Queue:", list(queue))

# The first served is queue[0], second served is queue[1]
second_served = queue[1]
print("Patient served second:", second_served)

Output:
Queue: [1, 2, 3, 4, 5]
Patient served second: 2

Challenge: Queue vs stack for graduation ceremony seating. Which is right?
Algorithmic reasoning:

Graduation ceremonies require that guests be seated in the order they arrive.

This is a First In, First Out (FIFO) scenario — those who arrive first get seated first.

A queue perfectly models this behavior: people join at the back and are served from the front.

A stack is LIFO — last to arrive would be served first, which is unfair in this context.

Answer: A queue is the right data structure for graduation seating because it ensures fairness by seating people in their arrival order.

Reflection: Why FIFO ensures fairness in ceremonies?

FIFO ensures fairness because it serves people in the exact order they arrive. This avoids cutting in line or skipping people, which can cause frustration and disputes. By maintaining a strict arrival order, everyone is treated equally and predictably. This principle is crucial in ceremonies, public services, and many real-life scenarios to maintain trust and order.
