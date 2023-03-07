Given an non-negative integer n. You are only allowed to make set bit unset. 
You have to find the maximum possible value of query so that after performing the given operations, 
no three consecutive bits of the integer query are set-bits. 
def noConseBits(self, n : int) -> int:
    # code here
    # divide the number by 2 consecutively and add the digits in arr 
    # 111101 -> 101101 
    # 101111 -> 101101 
    # if 3 1s are formed then break the 3rd one

    bin_arr = list(str(bin(n))[2:])

    # print(bin_arr)

    ones_freq = 0

    for i in range(len(bin_arr)):
        if bin_arr[i] == "1":
            ones_freq += 1
        else:
            ones_freq = 0

        if ones_freq == 3:
            bin_arr[i] = "0"
            ones_freq = 0

    return int("".join(bin_arr), 2)
