"""时间工具"""
class TimeHelper:

    @staticmethod
    def str2timestmap(time_str: str, time_format: str) -> int:
        """时间字符串转13位时间戳

        Args:
            time_str (str): 时间字符串
            time_format (str): 格式化标准

        Returns:
            int: 13位时间戳
        """

    @staticmethod
    def timestamp2str(timestamp: int, time_format: str) -> str:
        """13位时间戳转时间字符串

        Args:
            timestamp (int): 13位时间戳
            time_format (str): 格式化标准

        Returns:
            str: 时间字符串
        """
