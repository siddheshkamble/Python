import os

def Write_File(FileName):
    if(os.path.exists(FileName)):
        print("Enter the data that you want to write in file")
        Data = input()

        fd = open(FileName, "a")  #a for append so data dont override
        fd.write(Data)

    else:
        print("File is not exising")
        return

def main():
    print("Enter the file name to write")
    Name = input()

    Write_File(Name)

if __name__ == "__main__":
    main()