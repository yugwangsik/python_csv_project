import csv
import re
import sys


def pull_txt(_data_path):
	_d_path = _data_path + "/output.txt"

	f = open(_d_path, 'r')
	line = f.readline()
	line = line.split(",")
	
	
	i = 0
	j = 0
	listup = [[]]
	for data in line:
		if data != '':
			listup[j].append(data)
			i += 1
			if i == 169:
				j += 1
				listup.insert(j, [])
				i = 0

	
	return listup	



def indexHeader(_path):
	f = open(_path, 'r', newline='')
	data = f.readline()
	data = data.strip()
	data = re.sub("\'|\'","",data)
	data = data.split(",")
	
	f.close()
	return data



def make(_data_list, _search_header):
	h_find = _data_list[0]
	find_num = [i for j in range(len(_search_header)) for i in range(len(h_find)) if _search_header[j] in h_find[i]]

	find_num = set(find_num)
	find_num = list(find_num)
	find_num = sorted(find_num)
	
	cnt = 0
	result_list = [[]]
	for i in range(len(_data_list)-1):
		for j in find_num:
			result_list[cnt].append(_data_list[cnt][j])
		cnt += 1
		result_list.insert(cnt,[])

	
	
	return result_list



def save_f(_result, __data_path, __search_header):
	__d_path = __data_path + "/select_search.csv"

	with open(__d_path, "w", newline='') as f:
		writer = csv.writer(f)
		for data in _result:
			writer.writerow(data)
	f.close()

	print("선택한 헤더에 해당하는 데이터를 저장하였습니다.")
	print("선택한 헤더는 " + str(__search_header) + " 입니다.")
	print("경로는 " + __d_path + " 입니다.")
		



if __name__ == "__main__" :
	try:
		path = sys.argv[1] + '/search_header.txt'
		data_path = sys.argv[2]

		data_list = pull_txt(data_path)
		search_header = indexHeader(path)

		result = make(data_list, search_header)
		save_f(result, data_path, search_header)
	except Exception as e:
		print("Error: index_header_field.py")
		print("경로를 찾을 수 없습니다.")





