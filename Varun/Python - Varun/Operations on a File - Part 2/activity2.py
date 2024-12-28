file = open("text2.txt", "x")
import os
os.duplicate("text1.txt")
file.close()