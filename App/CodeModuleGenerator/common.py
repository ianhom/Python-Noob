# Common defines for CMG

# MACRO
mif   = "#if "
mels  = "#else "
mend  = "#endif\n"
mdf   = "#define "
mundf = "#undef "
mifd  = "#ifdef "
mifnd = "#ifndef "
minc  = "#include "
mpck1 = "#pack(1)"
mpck4 = "#pack(4)"
mpop  = "#pop"
mpush = "#push"


# End of file and make sure there is a blank line
file_end = "End of file\n"

# Code segments
def hhead(name):
    return mifnd + name "\n" + mundf + name + "\n" + mend
