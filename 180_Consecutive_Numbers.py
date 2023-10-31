# https://leetcode.com/problems/consecutive-numbers/

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    num_list = list(logs["num"])
    res = set()
    if len(num_list) > 2:
        num_list.append(num_list[-1] + 1)
        cnt = 1
        current_num = num_list[0]
        for i in range(1, len(num_list)):
            if num_list[i] == current_num:
                cnt += 1
            else:
                if cnt >= 3:
                    res.add(current_num)
                cnt = 1
                current_num = num_list[i]
    return pd.DataFrame({"ConsecutiveNums": list(res)})
