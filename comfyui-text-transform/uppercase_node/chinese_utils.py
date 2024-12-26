class ChineseNumberConverter:
    def __init__(self):
        self.CN_NUM = {
            '〇': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
            '六': 6, '七': 7, '八': 8, '九': 9, '零': 0,
            '壹': 1, '贰': 2, '叁': 3, '肆': 4, '伍': 5,
            '陆': 6, '柒': 7, '捌': 8, '玖': 9
        }
        
        self.CN_UNIT = {
            '十': 10, '拾': 10,
            '百': 100, '佰': 100,
            '千': 1000, '仟': 1000,
            '万': 10000, '萬': 10000,
            '亿': 100000000, '億': 100000000
        }
        
        self.CN_MONEY = {
            0: '零', 1: '壹', 2: '贰', 3: '叁', 4: '肆',
            5: '伍', 6: '陆', 7: '柒', 8: '捌', 9: '玖'
        }
        
        self.CN_MONEY_UNIT = ['', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿']

    def to_chinese_number(self, number):
        """将数字转换为中文数字"""
        if not isinstance(number, (int, float, str)):
            return str(number)
        
        number = float(number)
        if number.is_integer():
            number = int(number)
        
        if number < 0:
            return f"负{self.to_chinese_number(abs(number))}"
        
        if number < 10:
            return self.CN_MONEY[number]
            
        result = ''
        num_str = str(number)
        length = len(num_str)
        
        for i, digit in enumerate(num_str):
            if digit == '.':
                break
            if digit == '0':
                if i + 1 < length and num_str[i + 1] != '0':
                    result += '零'
            else:
                result += self.CN_MONEY[int(digit)]
                if i < length - 1:
                    result += self.CN_MONEY_UNIT[length - 1 - i]
                    
        return result

    def to_arabic_number(self, cn_string):
        """将中文数字转换为阿拉伯数字"""
        result = 0
        tmp = 0
        unit = 1
        
        for char in reversed(cn_string):
            if char in self.CN_NUM:
                tmp = self.CN_NUM[char]
            elif char in self.CN_UNIT:
                unit = self.CN_UNIT[char]
                result += tmp * unit
                tmp = 0
            else:
                tmp = 0
                
        result += tmp
        return str(result)

    def to_money_upper(self, number):
        """将数字转换为中文金额大写"""
        try:
            number = float(number)
        except ValueError:
            return "输入必须是数字"
            
        if number > 999999999999.99:
            return "数额过大"
            
        integer_part = int(number)
        decimal_part = round((number - integer_part) * 100)
        
        integer_str = self.to_chinese_number(integer_part)
        result = f"{integer_str}元"
        
        if decimal_part > 0:
            jiao = decimal_part // 10
            fen = decimal_part % 10
            if jiao > 0:
                result += f"{self.CN_MONEY[jiao]}角"
            if fen > 0:
                result += f"{self.CN_MONEY[fen]}分"
        else:
            result += "整"
            
        return result 