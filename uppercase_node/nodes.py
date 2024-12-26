from .chinese_utils import ChineseNumberConverter

class TextTransformNode:
    def __init__(self):
        self.cn_converter = ChineseNumberConverter()
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True}),
                "transform_type": ([
                    "UPPERCASE", 
                    "lowercase", 
                    "Title Case", 
                    "Sentence case", 
                    "aLtErNaTiNg CaSe",
                    "数字转中文",  # 阿拉伯数字转中文数字
                    "中文数字转阿拉伯",  # 中文数字转阿拉伯数字
                    "金额转大写",  # 数字金额转中文大写
                ],),
                "strip_whitespace": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "prefix": ("STRING", {"default": ""}),
                "suffix": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "transform_text"
    CATEGORY = "text"
    
    def transform_text(self, text, transform_type, strip_whitespace, prefix="", suffix=""):
        if strip_whitespace:
            text = text.strip()
            
        # 基础转换功能
        if transform_type == "UPPERCASE":
            result = text.upper()
        elif transform_type == "lowercase":
            result = text.lower()
        elif transform_type == "Title Case":
            result = text.title()
        elif transform_type == "Sentence case":
            result = text.capitalize()
        elif transform_type == "aLtErNaTiNg CaSe":
            result = ''.join(c.upper() if i % 2 == 0 else c.lower()
                           for i, c in enumerate(text))
        # 中文数字转换功能
        elif transform_type == "数字转中文":
            result = self.cn_converter.to_chinese_number(text)
        elif transform_type == "中文数字转阿拉伯":
            result = self.cn_converter.to_arabic_number(text)
        elif transform_type == "金额转大写":
            result = self.cn_converter.to_money_upper(text)
            
        result = f"{prefix}{result}{suffix}"
        return (result,)

NODE_CLASS_MAPPINGS = {
    "TextTransform": TextTransformNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextTransform": "Text Transform"
} 