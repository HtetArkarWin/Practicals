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
    ext_to_category={}
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        ext = os.path.splitext(filename)[1].replace(".","")
        if not (ext in ext_to_category.keys()):
            new_category = str(input('What category would you like to sort {} files into?'.format(ext))).strip()
            ext_to_category[ext]=new_category

        category=ext_to_category[ext]
        if not os.path.exists(category):
            try:
                #print('creating {}'.format(category))
                os.mkdir(category)
            except FileExistsError:
                print(category + ' directory already exist.')

        new_name=os.path.join(category, filename)
        #print("Moving {} to {}".format(filename, new_name))

        shutil.move(filename, new_name)

main()