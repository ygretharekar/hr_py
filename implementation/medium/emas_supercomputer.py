"""https://www.hackerrank.com/challenges/two-pluses/problem"""


class EmaSupercomputer:

    @staticmethod
    def within_range(rows, cols, i, j):
        return 0 <= i < rows and 0 <= j < cols

    @staticmethod
    def solution(grid):

        rows = len(grid)

        if not rows:
            return 0

        cols = len(grid[0])

        grid_pluses = []

        for i in range(rows):
            # pluses = []
            for j in range(cols):
                plus_dict = dict()
                up = down = left = right = 0

                if grid[i][j] != 'G':
                    plus_dict['i'] = i
                    plus_dict['j'] = j
                    plus_dict['length'] = 0
                    plus_dict['area'] = 0

                    grid_pluses.append(plus_dict)

                    continue

                temp_i = i - 1
                temp_j = j
                while EmaSupercomputer.within_range(rows, cols, temp_i, temp_j):
                    if grid[temp_i][temp_j] == 'G':
                        up += 1
                        temp_i -= 1
                    else:
                        break

                temp_i = i + 1
                temp_j = j
                while EmaSupercomputer.within_range(rows, cols, temp_i, temp_j):
                    if grid[temp_i][temp_j] == 'G':
                        down += 1
                        temp_i += 1
                    else:
                        break

                temp_i = i
                temp_j = j - 1
                while EmaSupercomputer.within_range(rows, cols, temp_i, temp_j):
                    if grid[temp_i][temp_j] == 'G':
                        left += 1
                        temp_j -= 1
                    else:
                        break

                temp_i = i
                temp_j = j + 1
                while EmaSupercomputer.within_range(rows, cols, temp_i, temp_j):
                    if grid[temp_i][temp_j] == 'G':
                        right += 1
                        temp_j += 1
                    else:
                        break

                length = min(up, down, right, left)

                length1 = length

                while length1 >= 0:
                    small_plus_dict = plus_dict.copy()
                    small_plus_dict['i'] = i
                    small_plus_dict['j'] = j
                    small_plus_dict['length'] = length1
                    small_plus_dict['area'] = 4 * length1 + 1
                    grid_pluses.append(small_plus_dict)
                    length1 -= 1

                # else:
                #     plus_dict['i'] = i
                #     plus_dict['j'] = j
                #     plus_dict['length'] = length
                #     plus_dict['area'] = 4 * length + 1
                #     grid_pluses.append(plus_dict)

        sorted_pluses = sorted(grid_pluses, key=lambda x: x['area'], reverse=True)

        sorted_length = len(sorted_pluses)

        ans_max = 0

        for i in range(sorted_length - 1):
            for j in range(i + 1, sorted_length):

                a = sorted_pluses[i]
                b = sorted_pluses[j]

                if a['i'] == b['i'] and a['j'] == b['j']:
                    continue

                left_side = a['j'] > b['j']
                right_side = a['j'] < b['j']
                up_side = a['i'] > b['i']
                down_side = a['i'] < b['i']

                if up_side:
                    if left_side:
                        if (b['j'] + b['length'] >= a['j'] and a['i'] - a['length'] <= b['i']) \
                                or (b['i'] + b['length'] >= a['i'] and a['j'] - a['length'] <= b['j']):
                            continue

                        else:
                            ans_max = max(ans_max, a['area'] * b['area'])

                    elif right_side:
                        if (b['j'] - b['length'] <= a['j'] and a['i'] - a['length'] <= b['i']) \
                                or (b['i'] + b['length'] >= a['i'] and a['j'] + a['length'] >= b['j']):
                            continue

                        else:
                            ans_max = max(ans_max, a['area'] * b['area'])
                    #
                    # else:
                    #     if b['length'] + b['j'] >= a['j'] - a['length']:
                    #         continue
                    #
                    #     else:
                    #         ans_max = max(ans_max, a['area'] * b['area'])
                    else:
                        if b['i'] + b['length'] >= a['i'] - a['length']:
                            continue

                        elif b['i'] - b['length'] <= a['i'] + a['length']:
                            continue

                        else:
                            ans_max = max(ans_max, a['area'] * b['area'])

                elif down_side:
                    if left_side:
                        if (b['j'] + b['length'] >= a['j'] and a['i'] + a['length'] >= b['i']) \
                                or (b['i'] - b['length'] <= a['i'] and a['j'] - a['length'] <= b['j']):
                            continue

                        else:
                            ans_max = max(ans_max, a['area'] * b['area'])

                    elif right_side:
                        if (b['j'] - b['length'] <= a['j'] and a['i'] + a['length'] >= b['i']) \
                                or (b['i'] - b['length'] <= a['i'] and a['j'] + a['length'] >= b['j']):
                            continue

                        else:
                            ans_max = max(ans_max, a['area'] * b['area'])

                    # else:
                    #     if b['j'] - b['length'] <= a['j'] + a['length']:
                    #         continue
                    #
                    #     else:
                    #         ans_max = max(ans_max, a['area'] * b['area'])

                    else:
                        if b['i'] - b['length'] <= a['i'] + a['length']:
                            continue

                        elif b['i'] + b['length'] >= a['i'] - a['length']:
                            continue

                        else:
                            ans_max = max(ans_max, a['area'] * b['area'])

                else:
                    if b['j'] + b['length'] < a['j'] - a['length']:
                        ans_max = max(ans_max, a['area'] * b['area'])

                    elif b['j'] - b['length'] > a['j'] + a['length']:
                        ans_max = max(ans_max, a['area'] * b['area'])

        return ans_max

    # if ans:
    #     multi = sorted_pluses[i]['area'] * sorted_pluses[j]['area']
    #
    #     if multi > ans_max:
    #         ans_max = multi

    # break_flag = True
    # break

# if break_flag:
#     break

# ans = False
# # if sorted_pluses[i]['area'] * sorted_pluses[j]['area'] > ans_max:
#
# if sorted_pluses[i]['j'] == sorted_pluses[j]['j']:
#     ans = ans or sorted_pluses[i]['i'] - sorted_pluses[i]['length'] > sorted_pluses[j]['i'] \
#         + sorted_pluses[j]['length']
#
#     ans = ans or sorted_pluses[i]['i'] + sorted_pluses[i]['length'] < sorted_pluses[j]['i'] \
#         - sorted_pluses[j]['length']
#
#     if ans:
#         ans_max = max(ans_max, sorted_pluses[i]['area']*sorted_pluses[j]['area'])
#
# elif sorted_pluses[i]['i'] == sorted_pluses[j]['i']:
#     ans = ans or sorted_pluses[i]['j'] - sorted_pluses[i]['length'] > sorted_pluses[j]['j'] \
#         + sorted_pluses[j]['length']
#
#     ans = ans or sorted_pluses[i]['j'] + sorted_pluses[i]['length'] < sorted_pluses[j]['j'] \
#         - sorted_pluses[j]['length']
#
#     if ans:
#         ans_max = max(ans_max, sorted_pluses[i]['area']*sorted_pluses[j]['area'])
#
# else:
