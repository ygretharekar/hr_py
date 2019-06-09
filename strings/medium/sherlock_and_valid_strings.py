class SherlockAndValidString:
    @staticmethod
    def solution(s):
        # str_set = set(s)

        # elif len(s) % (len(str_set) - 1) == 0:
        #     return "YES"

        from collections import Counter

        char_count = Counter(s)

        count_count = Counter(char_count.values())

        if len(count_count) == 1:
            return "YES"

        elif len(count_count) == 2:
            if (list(count_count.keys())[0] == 1 and list(count_count.values())[0] == 1) or \
                    (list(count_count.keys())[1] - list(count_count.keys())[0] == 1 and
                        count_count[list(count_count.keys())[1]] == 1) or \
                    (list(count_count.keys())[1] == 1 and list(count_count.values())[1] == 1) or \
                    ((list(count_count.keys())[0] - list(count_count.keys())[0]) == 1 and
                        count_count[list(count_count.keys())[0]] == 1):
                return "YES"

            else:
                return "NO"

        # if len(s) % len(str_set) == 0 or len(s) % len(str_set) == 1:
        #     return "YES"
        # elif (len(s) - 1) % (len(str_set) - 1) == 0:
        #     return "YES"
        else:
            return "NO"
