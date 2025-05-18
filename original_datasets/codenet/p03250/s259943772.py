if __name__ == '__main__':
    input_list = sorted(map(int, input().split()), reverse=True)

    print(str(input_list[0]*10 + input_list[1] + input_list[2]))