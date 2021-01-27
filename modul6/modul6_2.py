# file operations
# from time import sleep
# #open('/Users/emanuel.craciun/PycharmProjects/PEP20G06/modul6/my_text')
# file = open('my_text', 'w')
# file.write('new text')
# file.close()
# #print(type(file))
# sleep(3)
#
# with open('my_text', 'w') as file2:
#     file2.write('new text2')

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
    2/0

    ''.split()