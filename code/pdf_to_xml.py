from subprocess import call
from os import listdir
from os import stat

pdf_directory = '../full'

count = 0
for f in listdir(pdf_directory):
    file_name = pdf_directory + '/' + f
    call(['pdftohtml', '-c', '-i', '-xml', file_name])
    count += 1
    if(count % 100 == 0):
        print("Done with: " + str(count) + " files.")
