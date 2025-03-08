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

def main()->None:
    height: int = 5
    ways: int = climbing_stairs_recur(height=height)
    print(f"There are {ways} ways to reach the top of {height} stairs, climbing either 1 or 2 stairs at a time")

if __name__ == "__main__":
    main()