from PIL import Image
from os import listdir
from os.path import splitext
from cairosvg import svg2png

target_directory = '.'
target = '.png'

for file in listdir(target_directory):
    filename, extension = splitext(file)
    try:
        if extension not in ['.py', target, '.svg']:
            im = Image.open(filename + extension)
            im.save(filename + target)
            print("+")
        if extension == '.svg':
        	svg2png(file_obj=open(filename + extension, 'rb'), write_to=filename + target)
        	
    except OSError:
        print('Cannot convert %s' % file)
