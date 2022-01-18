# -*- coding: utf-8 -*-
import os
import csv
import re

def search_dir(dir_path, _filelist, _dirlist):
    
    if os.path.isfile(dir_path):                                    #해당 디렉토리에 csv파일이 있는지 판단
        file_extension = os.path.splitext(dir_path)[1]              #splitext()[1] 확장자만 반환  but, splitext() 전체경로 및 확장자까지 반환
        if file_extension == ".csv" or file_extension == ".CSV":    #확장자가 .csv 혹은 .CSV라면 실행
            _filelist.append(dir_path)                              #csv파일 list에 추가
            # print(_filelist)
        return None

    dir_list = []
    f_list = os.listdir(dir_path)                                   #현재 경로에 모든 파일 및 디렉토리 반환
    # print(f_list)
    for fname in f_list:                                            
        file_extension = os.path.splitext(fname)[1]                 #리스트에서 확장자만 가져와서 변수에 저장
        if os.path.isdir(dir_path + "/" + fname):                   #dir_path에 디렉토리가 있으면 실행
            dir_list.append(dir_path + "/" + fname)                 #dir_path list에 저장
            _dirlist.append(dir_path + "/" + fname)
            # print(dir_list)
        elif os.path.isfile(dir_path + "/" + fname):                #혹은 dir_path에 파일이 있으면 실행
            if file_extension == ".csv" or file_extension == ".CSV":#file_extension이 .csv 혹은 .CSV라면 실행
                _filelist.append(dir_path + "/" + fname)            #_filelist에 저장
                # print(_filelist)
                return None

    for toDir in dir_list:                                          #dir_list만큼 실행(재귀)
        search_dir(toDir, _filelist, _dirlist)


if __name__== "__main__" :
    
    file_list = []
    dir_list = []
    _f_limit=1000 
    csvpath = "/home/gwangsik/python_csv_project"                       #로컬경로

    search_dir(csvpath, file_list, dir_list)                    #디렉토리에 csv파일이 존재하는가 판단 & 경로 저장
    # print(file_list)
    f_name = str(file_list)
    f_name = re.sub("\[|\]|\'","",f_name)
    f = open(f_name,'r', encoding='UTF8')
    rdr = csv.reader(f)

    csv_list = []
    print(type(rdr))

    for line in rdr:
        csv_list.append(line)

    print(csv_list[2])

    f.close()

