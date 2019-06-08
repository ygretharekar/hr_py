class AlmostSorted:
    @staticmethod
    def check_sorted(arr):
        return all([i <= j for i, j in zip(arr[:-1], arr[1:])])

    @staticmethod
    def solution(arr):
        right = len(arr)
        left = -1

        if right == 1 or AlmostSorted.check_sorted(arr):
            print("yes")
            return

        for i, tup in enumerate(zip(arr[:-1], arr[1:])):
            if tup[0] > tup[1]:
                left = i
                break

        for i, tup in enumerate(zip(arr[-1:0:-1], arr[-2::-1])):
            if tup[0] < tup[1]:
                right = len(arr) - 1 - i
                break

        if left == right:
            print("no")
            return

        if right < len(arr) and left > -1:
            arr[left], arr[right] = arr[right], arr[left]
            if AlmostSorted.check_sorted(arr):
                print("yes")
                print(f"swap {left + 1} {right + 1}")
                return

            t_left = left + 1
            t_right = right - 1

            while t_left < t_right:
                arr[t_left], arr[t_right] = arr[t_right], arr[t_left]
                t_left += 1
                t_right -= 1

            if AlmostSorted.check_sorted(arr):
                print("yes")
                print(f"reverse {left + 1} {right + 1}")

            else:
                print("no")

        return
