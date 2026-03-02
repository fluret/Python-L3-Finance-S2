from compress_list import compress
from compress_list2 import compress as compress2


assert list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0,  0])) == [5, 4, 5, 6, 5, 7, 8, 0]
assert list(compress([1, 1, 1, 1, 2, 2,2, 1, 1, 1])) == [1, 2, 1]
assert list(compress([7, 7])) == [7]
assert list(compress([])) == []
assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
print("All tests for compress 1 passed!")

assert list(compress2([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0,  0])) == [5, 4, 5, 6, 5, 7, 8, 0]
assert list(compress2([1, 1, 1, 1, 2, 2,2, 1, 1, 1])) == [1, 2, 1]
assert list(compress2([7, 7])) == [7]
assert list(compress2([])) == []
assert list(compress2([1, 2, 3, 4])) == [1, 2, 3, 4]
assert list(compress2([9, 9, 9, 9, 9, 9, 9])) == [9]
print("All tests for compress version two passed!")