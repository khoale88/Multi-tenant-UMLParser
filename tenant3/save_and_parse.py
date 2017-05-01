import subprocess
import os

def process(jar_path, save_path, data, output_path):
    """save data into a file in save_path directory as sequence.java
    and parse the file with output saved in output_path"""

    #get the absolute path of save_path and output_path
    save_path = os.path.abspath(save_path)
    output_path = os.path.abspath(output_path)
    file_name = "sequence"
    file_ext = ".java"

    #save data to folder and get the whole path
    seq_path = save_to_folder(save_path, file_name + file_ext, data)
    #parse the file
    parse_uml(jar_path, seq_path)

    #move file from save_path directory to output_path folder and rename to output.png
    ori = os.path.join(save_path, file_name + ".png")
    des = os.path.join(output_path, "output.png")

    os.rename(ori, des)

    return des


def parse_uml(jar_path, input_path):
    """parse_uml needs 2 inputs: a path to parser file,
    and an input_path to folder where sequence file resides.
    the result is store in the same input_path directory"""

    subprocess.call(["java", "-jar", jar_path, "--headless", input_path])

def save_to_folder(save_path, save_name, data):
    """save data into a file in save_path directory with name given by save_name
    return the path to the file"""

    path = os.path.join(save_path, save_name)
    myfile = open(path, "w")
    myfile.write(data)
    myfile.close()
    return path

