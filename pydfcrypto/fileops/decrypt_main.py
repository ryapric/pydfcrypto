#!/usr/bin/env python3
import pydfcrypto.fileops.fileops as fileops
import sys

def main():
    for i in sys.argv:
        fileops.decrypt_file(i, cipher)

if __name__ == '__main__':
    main()
