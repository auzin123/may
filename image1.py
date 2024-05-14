import os

# путь к файлу который я запустил
print(__file__)

# путь к папке кде лежит файл который я запустил
currect_directory = os.path.dirname(__file__)

# путь к изображению
print(os.path.join(currect_directory, 'image', '100.png2'))
