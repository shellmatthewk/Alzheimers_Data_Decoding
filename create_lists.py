list_1 = list(range(1, 89))
string_list = [f'sub-00{i}\n' if i < 10 else f'sub-0{i}\n' for i in list_1]
with open('participant_list.txt', 'w') as file:
    file.writelines(string_list)

