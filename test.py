from itertools import combinations

def find_min_columns(matrix, n, m):
    columns = list(range(m))
    for k in range(1, m + 1):
        for comb in combinations(columns, k):
            # Check if this combination of columns has at least one 0 in each row
            if all(any(matrix[i][j] == 0 for j in comb) for i in range(n)):
                return k, comb
    return "Impossible", None

def main():
    # Input reading
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    # Find the solution
    result, columns = find_min_columns(matrix, n, m)
    
    # Output the result
    if result == "Impossible":
        print(result)
    else:
        print(result)
        print(" ".join(str(col + 1) for col in columns))

if __name__ == "__main__":
    main()
