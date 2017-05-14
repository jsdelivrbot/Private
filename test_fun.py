from linereader import dopen
from random import randint

f_firstname = dopen('random\\ten-nam.txt')
	print(f_firstname.getline(randint(1, f_firstname.count('\n'))))