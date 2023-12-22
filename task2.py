
# Исходные данные
list_version = [[‘665587’, 2], [‘669532’, 1], [‘669537’, 2], [‘669532’, 1], [‘665587’, 1]]

grouped_data = {}

for item in list_version:
    user_id, version = item
    key = (user_id, version)

    if key not in grouped_data:
        grouped_data[key] = []

    grouped_data[key].append(item)

result_list = list(grouped_data.values())

print(result_list)
