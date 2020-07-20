def remove_newlines(fname):
    flist = open(fname).readlines()
    clean_list = [s.rstrip('\n') for s in flist]
    
    file = open(fname, "w")
    for i in clean_list:
        file.write(i) 
    file.close() 
