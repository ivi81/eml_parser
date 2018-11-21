# -*- coding: utf8 -*-
#!/usr/bin/python3
""" 
    Консольный интерфейс для поиска в сетевом трафике email и анализа их вложений  
"""
import argparse
import pexpect
import sys
sys.path.append('../')
import json

import _smtp_processor
import indexfiles

if __name__ == '__main__' :
    
    with open( 'init_test/test_settings.json','r') as fp:
        settings = json.load(fp)
    print (type(sys.stdin))

    smtp_handlers_collection = _smtp_processor.SMTPHandlersCollection()

    '''Обработка тестового набора eml файлов (acii)'''
    '''  
    ifiles=indexfiles.SimpleIndexFiles()
    ifiles.add_recursive_path("./eml")
    for file in ifiles.get_paths("*.eml"):
        with open (file,"rb") as stream:
           eml_.processing_stream(stream)
    '''
    '''Обработка тестового набора tdp файлов (binary)'''
    ifiles=indexfiles.SimpleIndexFiles()
    print(settings['traffick_path'])
    ifiles.add_recursive_path(settings['traffick_path'])
    for file in ifiles.get_paths(".tdp"):
        with open (file,"rb") as stream:
           smtp_handlers_collection.processing_stream(stream)