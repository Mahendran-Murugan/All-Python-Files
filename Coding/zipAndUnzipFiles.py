from zipfile import ZipFile

with ZipFile('binary.zip', 'w') as archive:
    archive.write('pickle.bin')
    archive.write('mahi.txt')

with ZipFile('binary.zip', 'w') as archive:
    archive.extractall()
