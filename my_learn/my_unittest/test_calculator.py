import unittest
# 导入我们要测试的功能
from python_learn.my_learn.calculator import add, divide

# 1. 必须继承 my_unittest.TestCase
class TestCalculator(unittest.TestCase):

    # 2. 测试固件：每次执行具体的测试方法“前”都会自动运行
    def setUp(self):
        print("\n--- 准备开始一个测试用例 ---")

    # 3. 测试固件：每次执行具体的测试方法“后”都会自动运行
    def tearDown(self):
        print("--- 一个测试用例执行结束 ---")

    # 4. 测试方法：名字必须以 test_ 开头！否则 my_unittest 不理你
    def test_add_success(self):
        """测试普通的加法功能"""
        result = add(1, 2)
        # 使用断言方法比对结果：预期结果是 3
        self.assertEqual(result, 4)

    def test_add_negative(self):
        """测试负数加法"""
        self.assertEqual(add(-1, -1), -2)

    def test_divide_by_zero(self):
        """测试除以0时，是否会如期抛出 ValueError 异常"""
        with self.assertRaises(ValueError):
            divide(10, 0)

# 5. 启动测试
if __name__ == "__main__":
    unittest.main()