import shutil
import os

def main():
    # Change to desired directory
    os.chdir('FilesToSort')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists


    # Loop through each file in the (current) directory
    exts=[]
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        ext = os.path.splitext(filename)[1].replace(".","")
        if not (ext in exts):
            exts.append(ext)
            try:
                os.mkdir(ext)
            except FileExistsError:
                print(ext + ' directory already exist.')

        new_name=os.path.join(ext, filename)
        print("Moving {} to {}".format(filename, new_name))

        shutil.move(filename, new_name)

main()