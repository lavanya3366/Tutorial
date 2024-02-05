#python file modes are- 'r'->Open a file for reading(default)
#'w'->open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
#'x'->Open a file for exclusive creation. If the file already exists, the operation fails
#'a'->Open for appending at the end of the file without truncating it. Creates a new file if it does not exists
#'t'->Open in text mode.
#'b'->Open in binary mode
#'+'->Open a file for updating(reading and writing)

#sample code->
#f1=open("employee.dat") ->equivalent to 'r' or 'rt'
#f2=open("pic.jpg",'r+b') ->read and write in binary mode
#f3=open("score.txt",'w) -> write in text mode
