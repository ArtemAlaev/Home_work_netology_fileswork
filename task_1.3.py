import os

# Получить список файлов в папке
files = os.listdir('C:\Users\User\Desktop\Home_work_netology_fileswork\task_1.3_unsorted')

# Создать список для хранения содержимого файлов
file_contents = []

# Прочитать содержимое каждого файла и добавить его в список
for file in files:
    with open(file, 'r') as f:
        content = f.readlines()
        file_contents.append((file, len(content), content))

# Отсортировать список по количеству строк в каждом файле
file_contents.sort(key=lambda x: x[1])

# Создать итоговый файл и записать содержимое
with open('solve_task_1.3.txt', 'w') as f:
    for file in file_contents:
        # Записать служебную информацию
        f.write(file[0] + '\n')
        f.write(str(file[1]) + '\n')
        
        # Записать содержимое файла
        for line in file[2]:
            f.write(line)
