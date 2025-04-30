from typing import List

def even_list(int_list: List[int]) -> List[int]:
    # TODO: 짝수만 골라낸 리스트를 반환
    pass

def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    # TODO: 짝수들의 제곱합을 반환
    pass

def main():
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

if __name__ == "__main__":
    main()