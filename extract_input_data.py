# -*- coding: utf-8 -*-
'''
    input folder: relative folder path to the root path where applications source code resides
    output file (in the root directory): descriptions/original_file_name.txt
'''

import re
import os


def extract_input(file_path, INPUT_PATTERN):
    input_list = []
    input_entry = ''
    f = open(file_path, encoding="utf8")
    line = f.readline()
    found_input = False

    while(line):
        stripped_line = line.strip()
        entry = re.search(INPUT_PATTERN, stripped_line)

        if entry is not None:
            found_input = True
            input_list.append(stripped_line)

        line = f.readline()

    assert found_input

    return input_list


def parse_input_line(input_entry):
    variable_name = ''
    data_type = ''
    title = ''
    description = ''
    # input_tuple = (variable_name, data_type, title, description)
    NAME_PATTERN = re.compile(r'name: ?((\".+?\")|(\'.+?\'))')
    TYPE_PATTERN = re.compile(r'type: ?((\".+?\")|(\'.+?\'))')
    TITLE_PATTERN = re.compile(r'title: ?((\".+?\")|(\'.+?\'))')
    DESCRIPTION_PATTERN = re.compile(r'description: ?((\".+?\")|(\'.+?\'))')
    PARAMETER = re.compile(r'([ \(:,]\".+?\" ?,??)|([ \(:,]\'.+?\' ?,??)')

    re_item_name = re.search(NAME_PATTERN, input_entry)
    if re_item_name is None:

        positional_parameters = ["".join(x) for x in re.findall(PARAMETER, input_entry)]
        print(positional_parameters)
        assert len(positional_parameters) >= 2
        variable_name = positional_parameters[0]
        # print(variable_name)
        data_type = positional_parameters[1]
        # print(data_type)
    else:
        # print(re_item_name.string)
        variable_name = input_entry[re_item_name.span()[0]+5:re_item_name.span()[1]]
        re_item_type = re.search(TYPE_PATTERN, input_entry)
        assert re_item_type is not None
        # print('hi')

        data_type = input_entry[re_item_type.span()[0]+5:re_item_type.span()[1]]
        # print(re_item_type.string)

    re_item_title = re.search(TITLE_PATTERN, input_entry)
    # print(re_item_title)
    if re_item_title is not None:
        title = input_entry[re_item_title.span()[0]+6:re_item_title.span()[1]]

    re_item_description = re.search(DESCRIPTION_PATTERN, input_entry)
    if re_item_description is not None:
        description = input_entry[re_item_description.span()[0]+12:re_item_description.span()[1]]

    return (variable_name, data_type, title, description)

def create_input_per_file(target_folder_relative_path):
    input_list = []
    script_dir = os.path.dirname(os.path.realpath(__file__))
    abs_target_folder_path = os.path.join(os.sep, script_dir, target_folder_relative_path)
    # print(abs)
    INPUT_PATTERN = re.compile(r'^input[ \(]')

    ff = open('input_per_file.txt', 'a+', encoding="utf8")

    for root, folder, _file in os.walk(abs_target_folder_path):
        for _file_name in _file:
            print(os.path.join(os.sep, abs_target_folder_path, _file_name))
            try:
                groovy_file = os.path.join(os.sep, abs_target_folder_path, _file_name)
                if not groovy_file.endswith('.groovy'):
                    continue
                ff.write(os.path.join(os.sep, abs_target_folder_path, _file_name))
                ff.write('\n')
                input_list = extract_input(groovy_file, INPUT_PATTERN)

                try:
                    for input_entry in input_list:
                        parsed_input_entry = parse_input_line(input_entry)
                        for item in parsed_input_entry:
                            ff.write(item)
                            ff.write('\n')
                        ff.write('\n')
                except AssertionError as e:
                    print('input parse assert error')
                    ff.write('not regular input mode: ')
                    ff.write(input_entry)
                    ff.write('\n')
                
            except AssertionError as e:
                print('assert error')
                ff.write('found NONE')
                ff.write('\n')
                # print(os.path.join(os.sep, abs_target_folder_path, _file_name))
                
    ff.close()


if __name__ == '__main__':
    create_input_per_file('smartThings/smartThings-SainT/smartThings-SainT-official')
    # input_entry = 'input "lock","capability.lock"'

    # for i in parse_input_line(input_entry):
    #     print(i)