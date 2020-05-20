# coding: utf-8
import nDnDICE

text = "3d100"

def main():
    result = nDnDICE.nDn(text)
    if result is not None:
        print(result)

if __name__ == "__main__":
    main()