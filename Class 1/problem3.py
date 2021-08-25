if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    first_max=-100;
    for x in arr:
        if x>first_max:
            first_max = x;
    second_max=-100;
    for x in arr:
        if x>second_max and x<first_max:
            second_max = x;        
    print(second_max)