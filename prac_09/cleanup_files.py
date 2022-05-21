"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        print('temp directory already exist.')

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    #TheHopeOfAllHearts.txt
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    result=""

    for index,letter in enumerate(filename):
        toappend=letter
        if index>0:
            prevLetter = filename[index-1]
            if letter.islower() and (prevLetter == "_" or prevLetter=="("):
                toappend=toappend.upper()

        if index<len(filename)-1:
            nextLetter=filename[index+1]
            if letter.islower() and nextLetter.isupper():
                toappend=toappend+ "_"

        result=result+toappend



    return result


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))


        for filename in filenames:
            new_name=os.path.join(directory_name, get_fixed_filename(filename))
            filename=os.path.join(directory_name, filename)
            print("Renaming {} to {}".format(filename,new_name))
            #os.rename(filename,new_name)

#main()
demo_walk()