import sys
import csv
import json
import pickle
import xml.etree.ElementTree as eTree
import os


def get_extention(random_string):
    return random_string.split(".")[-1]


def work_csv_inp(path):
    file = open(path, 'r')
    reader = csv.DictReader(file)
    python_obj = list(reader)
    file.close()
    return python_obj


def work_csv_outp(path, python_obj):
    headers = python_obj[0].keys()
    file = open(path, "w")
    writer = csv.DictWriter(file, headers)
    writer.writeheader()
    writer.writerows(python_obj)
    file.close()


def work_json_inp(path):
    file = open(path, 'r')
    python_obj = json.load(file)
    file.close()
    return python_obj


def work_json_outp(path, python_obj):
    file = open(path, 'w')
    file.write(json.dumps(python_obj, indent=4))
    file.close()


def work_pickle_inp(path):
    file = open(path, 'rb')
    python_obj = pickle.load(file)
    file.close
    return python_obj


def work_pickle_outp(path, python_obj):
    file = open(path, 'wb')
    pickle.dump(python_obj, file)
    file.close()


def work_xml_inp(path):
    file = open(path, 'r')
    tree = eTree.parse(file)
    root = tree.getroot()
    python_obj = []
    for user in root:
       python_obj.append({
           child.tag: child.text for child in user.getchildren()
                          })
    return python_obj


# def work_xml_outp(path, python_obj):



def run_logic(first_file, second_file=None):
    if not os.path.exists(first_file):
        raise SystemExit('Такого файла не существует')

    ext_first = get_extention(first_file)
    res_inp = extentions_inp[ext_first](first_file)
    if second_file == None:
        print(res_inp)
    else:
        ext_second = get_extention(second_file)
        extentions_out[ext_second](second_file, res_inp)


def main():
    _, *file_paths = sys.argv
    if len(file_paths) < 1:
        raise SystemExit("На входе должно быть от 1 до 2 файлов")
    run_logic(*file_paths)


extentions_inp = {
    'csv': work_csv_inp,
    'json': work_json_inp,
    'bin': work_pickle_inp,
    'xml': work_xml_inp
                  }
extentions_out = {
    'csv': work_csv_outp,
    'json': work_json_outp,
    'bin': work_pickle_outp,
                  }

if __name__ == "__main__":
    main()