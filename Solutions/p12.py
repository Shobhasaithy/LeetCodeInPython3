class Solution:
    def intToRoman(self, num: int) -> str:
        unit_place = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens_place = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hund_place = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thou_place = ["","M","MM","MMM"]

        return thou_place[num//1000] + hund_place[(num%1000)//100] + tens_place[(num%100)//10] + unit_place[num%10]

'''
Simple self explanatory code
'''
hello leetcode
