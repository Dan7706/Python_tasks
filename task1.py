

def verify_input(user_input, list_keys):
    # Здесь проверяем наличие ключа в списке
    if user_input in list_keys:
        # а здесь проверяем открывающие и закрывающие скобки
        if user_input.count('(') == user_input.count(')'):
            return True, f"{user_input} - корректно"
    else:
        return False, f"{user_input} - некорректно"

list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']
user_input = input("Enter your information: ")

result, message = verify_input(user_input, list_keys)

if result:
    print(message)
else:
    print(message)
