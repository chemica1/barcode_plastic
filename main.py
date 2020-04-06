import winsound
import os
from File_class import File_class


def main():
    dir_path = os.getcwd()
    barcode_list = []
    name_list = []
    tmp_barcode = File_class('barcode').call_the_list()  # 바코드리스트
    for i in range(1,int(len(tmp_barcode)/2 + 1)) :
        barcode_list.append(tmp_barcode[(2*i-1)])  # txt에서 바코드 줄
        print(tmp_barcode[(2*i-1)])
    for i in range(0,int(len(tmp_barcode)/2)) :
        name_list.append(tmp_barcode[2*i])  # txt에서 이름
        print(tmp_barcode[2*i])
    n = '0'
    while len(n.strip()) > 0: ##아무 입력없이(or공백만입력하고) 엔터누르면 반복문 종료
        n = input()
        for i in range(0,len(barcode_list)):
            if n == barcode_list[i] :
                winsound.PlaySound(f'{dir_path}\\sound\\{name_list[i]}.wav',winsound.SND_FILENAME)


if __name__ == '__main__':
    main()
