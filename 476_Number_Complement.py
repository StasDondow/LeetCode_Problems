# https://leetcode.com/problems/number-complement

class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = self.intToBin(num)
        inverted_bin = self.invertBin(bin_num)
        return self.binToInt(inverted_bin)

    def intToBin(self, int_num):
        bin_num = ""
        while int_num > 1:
            bin_num = str(int_num % 2) + bin_num
            int_num = int_num // 2
        else:
            bin_num = "1" + bin_num
        return bin_num
    
    def binToInt(self, bin_num):
        int_num = 0
        power = 0
        while len(bin_num) > 0:
            if bin_num[-1] == "1":
                int_num += 2 ** power
            power += 1
            bin_num = bin_num[:-1]
        return int_num

    def invertBin(self, bin_num):
        inverted_bin = "".join(["1" if s == "0" else "0" for s in bin_num])
        return inverted_bin.lstrip("0")
