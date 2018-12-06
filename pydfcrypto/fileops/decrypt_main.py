#!/usr/bin/env python3
import pydfcrypto.fileops.helpers as dfh
import sys

def main():
    for i in sys.argv:
        dfh.decrypt_file(i)

if __name__ == '__main__':
    main()
