from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        pass

class QuickSortStrategy(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        # For demonstration, we'll just use built-in sort
        print("Using QuickSort strategy")
        return sorted(data)

class BubbleSortStrategy(SortStrategy):
    def sort(self, data: list[int]) -> list[int]:
        # Simplified bubble sort example (inefficient but illustrative)
        print("Using BubbleSort strategy")
        arr = data[:]
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

class SortContext:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort_data(self, data: list[int]) -> list[int]:
        return self.strategy.sort(data)

if __name__ == "__main__":
    quick_sort_context = SortContext(QuickSortStrategy())
    bubble_sort_context = SortContext(BubbleSortStrategy())

    data = [5, 2, 8, 1, 3]
    print(quick_sort_context.sort_data(data))   # Uses QuickSort
    print(bubble_sort_context.sort_data(data))  # Uses BubbleSort
