import os

def generator():    
    def folder_locator():
        directory = input("Desired flask folder name: ")
        parent_directory = input("Desired root directory (Leave blank to create in current directory): ")
        if len(parent_directory) ==  0:
            "" == parent_directory == os.getcwd 
        return folder_generator(directory, parent_directory)
    
    def folder_generator(directory,parent_directory):
        try:
            path = os.path.join(parent_directory, directory)
            os.mkdir(path)
        except FileExistsError:
            print(f"File name {directory} already exists in current directory")
            parent_directory = parent_directory
            directory = input("Desired flask folder name: ")
            return folder_generator(directory, parent_directory)
        except FileNotFoundError:
            print("Can't find root directory")
            directory = directory
            parent_directory = input("Desired root directory (leave blank for current directory): ")
            return folder_generator(directory, parent_directory)
        
        finally:
            print(f"{directory} was created in {parent_directory}")
    
    folder_locator()

generator()
