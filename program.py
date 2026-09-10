import os 

for name in os.listdir("."):
    print(name[:-4])
    try:
        if name != "program.py" :
            # os.rename(name, name+".mp4")
            os.rename(name, name[:-4])
        print(f"File '{name}' successfully renamed to '{name[:-4]}'.")
    except FileNotFoundError:
        print(f"Error: The file '{name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



