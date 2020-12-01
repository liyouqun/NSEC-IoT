# -*- coding: utf-8 -*-
'''
    input folder: relative folder path to the root path where applications source code resides
    output file (in the root directory): descriptions/original_file_name.txt
'''

import re
import os


def extract_description(file_path,
                        DEFINITION_PATTERN, 
                        END_DEFINITION_PATTERN, 
                        DESCRIPTION_PATTERN):
    # file_name = 'alfred-workflow.groovy'
    description_txt = ''
    f = open(file_path, encoding="utf8")
    line = f.readline()
    found_definition = False
    while(line):
        # print('1')
        # print(line)
        if re.match(DEFINITION_PATTERN, line):
            found_definition = True
            break
        line = f.readline()

    assert found_definition

    line = f.readline().strip()
    # print(line)

    found_description = False
    while(re.match(END_DEFINITION_PATTERN, line) is None):
        # print('2')
        description = re.search(DESCRIPTION_PATTERN, line)
        if description is not None:
            
            first_quotation_mark = line.find('"') + 1
            last_quotation_mark = len(line)-2

            description_txt = line[first_quotation_mark:last_quotation_mark]
            found_description = True
        line = f.readline().strip()

    f.close()
    assert found_description

    return description_txt



def create_description_txt_file(target_folder_relative_path):
    description_txt = ''
    script_dir = os.path.dirname(os.path.realpath(__file__))
    abs_target_folder_path = os.path.join(os.sep, script_dir, target_folder_relative_path)

    DEFINITION = re.compile(r' *definition ?\(')
    # END_DEFINITION = re.compile(r'^preferences')
    END_DEFINITION = re.compile(r'^def')
    DESCRIPTION = re.compile(r'^description:')

    ff = open('description_out.txt', 'a+', encoding="utf8")
    for root, folder, _file in os.walk(abs_target_folder_path):
        for _file_name in _file:
            # print(os.path.join(os.sep, abs_target_folder_path, _file_name))
            try:
                groovy_file = os.path.join(os.sep, abs_target_folder_path, _file_name)
                if not groovy_file.endswith('.groovy'):
                    continue
                ff.write(os.path.join(os.sep, abs_target_folder_path, _file_name))
                description_txt = extract_description(groovy_file, DEFINITION, END_DEFINITION, DESCRIPTION)
                # print(description_txt)
                ff.write('=='+description_txt)
                ff.write('\n')
            except AssertionError as e:
                print('assert error')
                print(os.path.join(os.sep, abs_target_folder_path, _file_name))
                ff.write('=='+description_txt)
                ff.write('\n')

    # file_path = os.path.join(os.sep, abs_target_folder_path, 'hue-lights-and-groups-and-scenes-oh-my.groovy')
    # text = extract_description(file_path, DEFINITION, END_DEFINITION, DESCRIPTION)
    # print(text)

    ff.close()

    

if __name__ == '__main__':
    create_description_txt_file('smartThings\smartThings-SainT\smartThings-SainT-official')
    # create_description_txt_file('smartThings\smartThings-SainT\smartThings-SainT-sensitive-data-leaks-benchmark-apps')
    create_description_txt_file('smartThings\smartThings-SainT\smartThings-SainT-third-party')
    # create_description_txt_file('smartThings\smartThings-ProvThings\ProvThings-attacks')
    # create_description_txt_file('smartThings\smartThings-Soteria\smartthings-Soteria-MalIoT-apps')
    create_description_txt_file('smartThings\smartThings-SainT\smartThings-Soteria-third-party')
    # # create_description_txt_file('smartThings\smartThings-contexIoT\smartThings-contexIoT-malicious-apps')
    create_description_txt_file('smartThings\smartThings-contexIoT\smartThings-contextIoT-official-and-third-party')


