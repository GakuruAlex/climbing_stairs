from typing import Dict
def climbing_stairs_recur(height: int) -> int:
    """_Find how many ways there are to reach the top of a staircase if you can only take ascend one or two levels at a time_

    Args:
        height (int): _Number of stairs_

    Returns:
        int: _Number of ways to get to the top_
    """
    if height == 2:
        return 2
    elif height == 1:
        return 1
    return climbing_stairs_recur(height - 2) + climbing_stairs_recur(height - 1)

def climbing_stairs_memo(height: int, memo: Dict[int, int] = {0:1, 1:1, 2: 2}) ->None:
    if height in memo:
        return memo[height]
    memo[height] = climbing_stairs_memo(height - 2, memo) + climbing_stairs_memo(height - 1, memo)
    return memo[height]

def climbing_stairs_tabulate(height: int) -> int:
    ways = [1, 1, 2]
    for way in range(3, height + 1):
        ways.append(ways[way -2] + ways[way - 1])
    return ways[height]

def main()->None:
    height: int = 4
    ways: int = climbing_stairs_tabulate(height=height)
    print(f"There are {ways} ways to reach the top of {height} stairs, climbing either 1 or 2 stairs at a time")
    ways: int = climbing_stairs_memo(height=height)
    print(f"There are {ways} ways to reach the top of {height} stairs, climbing either 1 or 2 stairs at a time")


if __name__ == "__main__":
    main()