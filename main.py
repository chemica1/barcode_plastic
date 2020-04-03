import winsound


def reversedString(s):
    return s[::-1]

def main():
    n = '0'
    while len(n.strip()) > 0: ##아무 입력없이(or공백만입력하고) 엔터누르면 반복문 종료
        n = input()
        print(reversedString(n))
        if n == '7610700009338':
            winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

if __name__ == '__main__':
    main()
