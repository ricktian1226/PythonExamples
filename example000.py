#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ricktian
#
# Created:     25/12/2017
# Copyright:   (c) ricktian 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
def main():
    if sys.version_info.major < 3:
        print("Version 2.X")
    elif sys.version_info.major > 3:
        print("Future")
    else:
        print("Version 3.x")
    pass

if __name__ == '__main__':
    main()
