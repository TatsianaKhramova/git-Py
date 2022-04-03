from hurry.filesize import size
import os

f = os.stat('text.txt').st_size

print(size(f))


