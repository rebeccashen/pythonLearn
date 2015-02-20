__author__ = 'rebeccashen'

import sys
write_file = file("write_file.txt", "w")
write_file.write("this is the first line of the file\n")
write_file.writelines(["and the second\n", "and the third.\n"])
write_file.close()