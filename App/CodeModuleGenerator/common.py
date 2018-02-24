# Common defines for CMG

# MACRO
mif   = "#if "
mels  = "#else "
mend  = "#endif "
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
def h_head_start(name):
    return mifnd + name "\n" + mdf + name + "\n"

def h_head_end(name):
    return mend + "/* " + name + " */" + "\n"

h_cpp_start = mifd + "__cplusplus\nextern \"C\" {\n" + mend + "\n"

h_cpp_end   = mifd + "} /* __cplusplus\n" + mend + "\n"
