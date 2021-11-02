# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:35:50 2021

@author: ouss3ma
"""

import argparse
import pandas as pd
import json
from convert_csv_to_json import convert_csv_to_json




def arg_parser():
    #parse arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('courses_file', type=str)
    parser.add_argument('students_file', type=str)
    parser.add_argument('tests_file', type=str)
    parser.add_argument('marks_file', type=str)
    parser.add_argument('output_file', type=str)

    return parser.parse_args()



def check_data(courses, students, tests, marks):
    json_out={}
    if (tests.groupby('course_id')['weight'].sum().mean()!=100):
        json_out = {"error": "Invalid course weights"}
        
    elif courses.isna().sum().sum():
        json_out = {"error": "course file has missing values"}
    elif students.isna().sum().sum():
        json_out = {"error": "student file has missing values"}
    elif tests.isna().sum().sum():
        json_out = {"error": "test file has missing values"}
    elif marks.isna().sum().sum():
        json_out = {"error": "mark file has missing values"}
        
    elif False in list(map(lambda x: str(x).isdigit(), tests['weight'])):
        json_out = {"error": "weight column in test file should be number"}
    elif False in list(map(lambda x: str(x).isdigit(), marks['mark'])):
        json_out = {"error": "mark column in mark file should be number"}
        
    elif False in list(tests['weight']>0):
        json_out = {"error": "weight should be a positive numbers"}
    elif False in list(marks['mark']>0):
        json_out = {"error": "mark should be a positive numbers"}
        
    return json_out


def main():
    """
    Args:
        args : {path-to-courses-file} {path-to-students-file} 
        {path-to-tests-file} {path-to-marks-file} {path-to-output-file}.
    """
    args = arg_parser()
    
    #read files
    courses = pd.read_csv(args.courses_file)
    students = pd.read_csv(args.students_file)
    tests = pd.read_csv(args.tests_file)
    marks = pd.read_csv(args.marks_file)

    #check files contents
    json_out = check_data(courses, students, tests, marks)
    if json_out:
        print("error!! check your JSON file for more informations")
    else:
        json_out = convert_csv_to_json(courses, students, tests, marks)
    
    with open(args.output_file, "w") as outfile:
        json.dump(json_out, outfile, indent=4)    
    
    print('JSON file created')
    
    
    
    
if __name__ == "__main__":
    main()   
    
 
