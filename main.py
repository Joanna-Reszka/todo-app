print('Enter a to do: ')
user_text = input()
print(user_text)

# better cause shorter
user_text = input('Enter a to do: ')
print(user_text)

# better cause easier to debug
message = 'Enter a to do: '
user_text = input(message)
print(user_text)

# multiple inputs simple
message = 'Enter a to do: '
text1 = input(message)
text2 = input(message)
text3 = input(message)
texts = [text1, text2, text3]
print(texts)

# multiple inputs with WHILE LOOP
message = 'Enter a to do: '
todos = []
while True:
    todo = input(message)
    if todo != "end":
        todos.append(todo.capitalize())
    else:
        break
    print(todos)
