from functools import reduce
from operator import mul

def parse(text: str):
    presents = []
    trees = []

    lines = text.split("\n")
    idx = 0
    shape_idx = 0

    while idx < len(lines):
        line = lines[idx].strip()
        if not line:
            continue

        if ":" in line and "x" in line:
            dims, counts = line.split(":")[0], line.split(":")[1]
            R, C = dims.strip().split("x")[0], dims.strip().split("x")[1]
            counts = [int(c) for c in counts.strip().split()]

            trees.append(((int(R), int(C)), counts))

        elif ":" in line:
            # present_idx = int(line.split(":")[0])
            shape_idx = idx + 1

            present = []
            while shape_idx < len(lines):
                if not lines[shape_idx].strip():
                    break

                present.append(lines[shape_idx].strip())
                shape_idx += 1

            presents.append(present)

        idx = max(idx+1, shape_idx+1)

    return presents, trees


def get_area(present: list[str]):
    return sum(line.count("#") for line in present)


def solve(present_to_area: dict[int, int], counts: list[int], size: tuple[int]):

    max_area = reduce(mul, size)
    print(f"max area: {max_area}")

    desired_area = 0
    for idx, count in enumerate(counts):
        desired_area += present_to_area[idx] * count

        if desired_area > max_area:
            return False

    return desired_area <= max_area


def part_one(text: str):

    presents, trees = parse(text)
    present_to_area = {idx: get_area(p) for idx, p in enumerate(presents)}

    results = []
    for tree_size, tree_counts in trees:
        results.append(solve(present_to_area, tree_counts, tree_size))
        print(f"tree {len(results)}: {results[-1]}")

    return sum(results)
