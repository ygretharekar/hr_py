class LarryArray:

    @staticmethod
    def solution(A):
        arr_len: int = len(A)

        inv = 0

        for i in range(arr_len):
            for j in range(i + 1, arr_len):
                if A[i] > A[j]:
                    inv += 1

        return "NO" if inv % 2 else "YES"
