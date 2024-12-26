# 从同目录下的nodes.py文件导入节点类映射和显示名称映射
from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# 声明可以被其他模块导入的变量名列表
# 这样其他模块可以通过 from uppercase_node import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS 来使用这些变量
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 