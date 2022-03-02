#!/usr/bin/env python3
#coding: utf-8
import os
import sys

def get_args():
    '''Gets all the arguments passed to the script and returns them in a parse_args()-type object.
    No args
    Returns:
    -args : an args object containing all the optional arguments passed to the script.
    '''
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", help = "Folder to search in", action="store", type=str, required=True)

    #Creating the args object
    args=parser.parse_args()

    return args

def spaceify(filepath):
    """Spaceify the file given by the absolute path filepath.
    """

    with open(filepath, "r") as myfile:
        myfile = myfile.read()

    myfile = myfile.replace("\t", "    ")
    with open(filepath, "w") as yourfile:
        yourfile.write(myfile)


args = get_args()
look_folder = args.folder
if look_folder[-1] == "/":
    look_folder = look_folder[:-1]

for thing in os.listdir(look_folder):
    fpath = f"{look_folder}/{thing}"
    if os.path.isfile(fpath):
        try:
            print(f"Working on {fpath}")
            spaceify(fpath)
        except Exception as e:
            print(f"Got exception {e} for {fpath}, sorry")
