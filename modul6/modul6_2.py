# file operations
from time import sleep

# open('/Users/emanuel.craciun/PycharmProjects/PEP20G06/modul6/my_text')
file = open('my_text', 'w')
file.write('new text')
file.close()
# print(type(file))
sleep(3)

with open('my_text', 'w') as file2:
    file2.write('new text2')


class FileWriter():
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path, 'x')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write('\n')
        self.file.close()
        return True


with FileWriter('new_file') as file:
    file.write('text')
    2 / 0


class FileWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        try:
            self.file = open(self.file_path, 'x')
        except FileExistsError:
            self.file = open(self.file_path, 'w')
        return self

    def get_code(self):
        my_string = input(">>>")
        indent = ['']
        while my_string or indent:
            if my_string.endswith(':'):
                indent.append(4 * ' ')
            my_string2 = input(f"...{''.join(indent)}")
            if not my_string2:
                indent.pop(-1)
            self.file.write(''.join(indent) + my_string + ("\n" if my_string2 else ""))
            my_string = my_string2

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write('\n')
        if exc_tb:
            self.file.write(str(exc_tb.tb_frame).split(',', 1)[1])
        self.file.close()
        return True


with FileWriter('new_file') as file:
    file.get_code()
