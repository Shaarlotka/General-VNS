def greedy_algorithm_vns(pure_ids, distances):
    return solution


def calculate_clusters(clusters, matrix, total_parts):
    in_clusters = 0
    for i in range(len(clusters[0])):
        for j in range(len(clusters[1])):
            if matrix[i][j] == 1 and clusters[i] == clusters[j]:
                in_clusters += 1
    return in_clusters / total_parts


def swap_2_opt(current_solution):
    return new_solution


def two_opt(solution):
    return solution


def convert(height, width):
    matrix = list()
    total_parts = 0
    for i in range(height):
        temp = [int(m) for m in input().split(' ')]
        matrix.append(list())
        index = 1
        for j in range(width):
            if index < len(temp) and j + 1 == temp[index]:
                matrix[i].append(1)
                index += 1
                total_parts += 1
            else:
                matrix[i].append(0)
    return matrix, total_parts


if __name__ == '__main__':
    quantity = input()
    quantity = [int(i) for i in quantity.split(' ')]
    matrix, total_parts = convert(quantity[0], quantity[1])
    print(matrix)
    clusters = list()
    clusters.append([0 for i in range(quantity[0])])
    clusters.append([0 for i in range(quantity[1])])
    print(clusters) # 1st line - machines, 2nd line - parts