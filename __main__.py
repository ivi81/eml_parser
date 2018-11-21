# -*- coding: utf8 -*-
#!/usr/bin/python3
""" 
    Консольный интерфейс для поиска в сетевом трафике email и анализа их вложений  
"""
#!/usr/bin/python3
import sys

import _smtp_processor 
import indexfiles

if __name__ == '__main__' :
    
    print (type(sys.stdin))

    eml_= smtp_processor.smtp.SMTPHandlersCollection()

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
    ifiles.add_recursive_path("./test_resource/traffic")
    for file in ifiles.get_paths("*.tdp"):
        with open (file,"rb") as stream:
           eml_.processing_stream(stream)