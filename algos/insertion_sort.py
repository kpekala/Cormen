def insertion_sort(A, n):
  for i in range(1, n):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
      A[j + 1] = A[j]
      j -= 1
    A[j + 1] = key
  return A

print(insertion_sort([2, 1, 3, 7], 4))
print(insertion_sort([7, 3, 2, 1], 4))
print(insertion_sort([1, 2, 3, 4], 4))