"""
When you read a file, the lines come with hidden characters like \n (new line). We need two tools to clean them:
1. .strip(): Removes the \n and spaces from the ends.
2. .split(): Breaks the line into a list of words/numbers based on spaces.
"""
line = "O  0.000  0.000  0.000 \n"
clean_line = line.strip()
parts = clean_line.split()

symbol = parts[0]
x = float(parts[1])
print(symbol)
print(x)
