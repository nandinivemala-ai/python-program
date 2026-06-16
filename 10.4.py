try:
    file=open("my file.txt","r")
except IOError:
    print("error:unable to read the file!")
finally:
    file.close()
