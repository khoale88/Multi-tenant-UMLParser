import subprocess
import zipfile
import os, shutil

def process(jar_path, save_path, zip_name, output_path):
    """upzip and parse function will unzip a compressed file, and use provided UML parser
    to parse such file. The result is stored in the output path"""

    #reformat the paths
    #save_path = os.path.abspath(save_path)
    #output_path = os.path.abspath(output_path)
    #shutil.rmtree(os.path.join(save_path, "output"))
    shutil.rmtree(save_path+"output")
    #unzip and parse the file.
    unzip_path = unzip_to_output_folder(save_path, zip_name)
    parse_uml(jar_path, unzip_path)

    #move file to output folder and rename to original name with .png
    ori = os.path.join(unzip_path, "output.png")
    des = os.path.join(output_path, "output.png")
    os.rename(ori, des)
    return des


def parse_uml(jar_path, input_path):
    """parse_uml needs 2 inputs: a path to parser file,
    an input_path to folder where java classes reside,
    result is stored in the same folder as input_path"""

    subprocess.call(["java", "-jar", jar_path, input_path, input_path + "/output.png"])

def unzip_to_output_folder(zip_path, zip_name):
    """rename the zip_file into output.zip
    and unzip it into "output" folder located in the same path as zip file"""

    #remane from xxx.zip to output.zip
    ori = os.path.join(zip_path, zip_name)
    des = os.path.join(zip_path, "output.zip")
    os.rename(ori, des)

    zipref = zipfile.ZipFile(des, "r")
    #get the folder and unzip
    des = des[:-4]
    zipref.extractall(des)
    zipref.close()
    #return the folder by excluding the '.zip'
    return des
