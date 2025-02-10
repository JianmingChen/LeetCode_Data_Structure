from typing import List
from collections import defaultdict
import heapq

class DataBlock:
    """数据块类，用于表示每个数据块"""
    def __init__(self, size: int):
        self.size = size
    
    def __lt__(self, other):
        return self.size < other.size

class ThreadDataBlocks:
    """线程数据块类，用于管理每个线程的数据块"""
    def __init__(self):
        self.blocks = []  # 用列表模拟链表，保持有序
    
    def add_block(self, size: int):
        """添加数据块，保持升序"""
        self.blocks.append(DataBlock(size))
        # 确保blocks按size升序排列
        self.blocks.sort(key=lambda x: x.size)

class DataBlockAnalyzer:
    """数据块分析器，用于统计所有线程的数据块分布"""
    def __init__(self):
        self.threads = defaultdict(ThreadDataBlocks)
    
    def add_thread_blocks(self, thread_id: int, sizes: List[int]):
        """添加一个线程的所有数据块"""
        for size in sizes:
            if not (1 <= thread_id <= 4096 and 1 <= size <= 2**16):
                raise ValueError("Invalid thread_id or block_size")
            self.threads[thread_id].add_block(size)
    
    def analyze_blocks(self) -> List[int]:
        """分析所有线程的数据块分布，返回升序且唯一的size列表"""
        heap = []
        
        # 将每个线程的第一个数据块放入堆中
        for thread_id, thread_blocks in self.threads.items():
            if thread_blocks.blocks:
                heapq.heappush(heap, (thread_blocks.blocks[0].size, thread_id, 0))
        
        result_set = set()
        
        while heap:
            size, thread_id, index = heapq.heappop(heap)
            result_set.add(size)
            
            if index + 1 < len(self.threads[thread_id].blocks):
                next_size = self.threads[thread_id].blocks[index + 1].size
                heapq.heappush(heap, (next_size, thread_id, index + 1))
        
        return sorted(list(result_set))

def process_input():
    """处理输入数据"""
    # 读取线程数量
    thread_count = int(input().strip())
    analyzer = DataBlockAnalyzer()
    
    # 读取每个线程的数据块
    for thread_id in range(1, thread_count + 1):
        # 读取并处理每行数据，转换为整数列表
        sizes = list(map(int, input().strip('[]').split(',')))
        analyzer.add_thread_blocks(thread_id, sizes)
    
    return analyzer.analyze_blocks()

def main():
    """主函数"""
    try:
        result = process_input()
        # 格式化输出
        print(f"[{','.join(map(str, result))}]")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
