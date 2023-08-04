class Solution:

    def get_word_representation_1(self, num):
        dictionary = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            0: "",
        }
        return dictionary[num]

    def get_word_representation_2(self, num):
        dictionary = {
            1: "Onty",
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
            0: "",
        }
        return dictionary[num]

    def get_word_representation_special(self, num):
        dictionary = {
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            10: "Ten",
        }
        return dictionary[num]

    def get_word_representation(self, num):
        if num == 0:
            return ""

        print (num)

        if ((num%100)//10 == 1):
            ans = ""
            if num//100 != 0:
                ans = " ".join([self.get_word_representation_1(num//100), "Hundred"])
            return " ".join([ans, self.get_word_representation_special(num%100)])

        ans = self.get_word_representation_1(num%10)
        ans = ans.strip()
        num = num//10
        if num == 0:
            return ans
        ans = " ".join([self.get_word_representation_2(num%10), ans])
        ans = ans.strip()
        num = num//10
        if num == 0:
            return ans
        ans = " ".join([self.get_word_representation_1(num%10), "Hundred", ans])
        ans = ans.strip()
        return ans

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        temp = num
        suffixes = ["", "Thousand", "Million", "Billion", "Trillion"]

        suffix_ind = 0
        ans = ""
        while temp > 0:
            remainder = temp%1000
            remainder_word_representation = self.get_word_representation(remainder)
            if remainder_word_representation != "":
                ans = " ".join([remainder_word_representation, suffixes[suffix_ind], ans])
            ans = ans.strip()
            temp = temp//1000
            suffix_ind = suffix_ind + 1

        # print (ans)
        return ans