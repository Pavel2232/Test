import os


def task1():
    # в папке test найти все файлы filenames вывести колличество
    result = []
    name_to_find ='filenames'
    for root, dirs, files in os.walk('test'):
        for filename in files:
            if name_to_find in filename:
                result.append(filename)
    print(len(result))


def task2():
    # в папке test найти все email адреса записанные в файлы
    emails = []
    email = '@'
    my_files = []
    for root, dirs, files in os.walk('test'):
        for filename in files:
            path_to = os.path.abspath(os.path.join(root, filename))
            if os.stat(path_to).st_size != 0:
                my_files.append(path_to)
                with open(root + '/' + filename, 'r') as file:
                    local_file = file.readlines()
                    for i in local_file:
                        if email in i:
                            emails.append(i)

    print(len(emails))


def main():
    task1()
    task2()
    # дополнительно: придумать механизм оптимизации 2-й задачи


if __name__ == '__main__':
    main()
