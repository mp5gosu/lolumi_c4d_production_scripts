import c4d, loutils
from c4d import gui

def main():
    loutils.convertMaterials(doc, loutils.MATCONV_VRAY)    

if __name__=='__main__':
    main()
