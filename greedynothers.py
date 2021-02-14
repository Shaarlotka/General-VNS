import random
import copy


def greedy_algorithm_vns(clusters, matrix):
    columns_sum = {index : 0 for index in range(len(clusters[1]))}
    rows_sum = {index : 0 for index in range(len(clusters[0]))}
    for i in range(len(clusters[0])):
        for j in range(len(clusters[1])):
            rows_sum[i] += matrix[i][j]
            columns_sum[j] += matrix[i][j]
    rows_sum = [(v, k) for k, v in rows_sum.items()]
    columns_sum = [(v, k) for k, v in columns_sum.items()]
    columns_sum.sort(key=lambda value: value[0], reverse=True)
    rows_sum.sort(key=lambda value: value[0], reverse=True)
    for i in range(len(clusters[0]) // 2 + len(clusters[0]) %2):
        clusters[0][rows_sum[i][1]] = 1
    for i in range(len(clusters[1]) // 2 + len(clusters[1]) %2):
        clusters[1][columns_sum[i][1]] = 1

    return clusters


def calculate_clusters(clusters, matrix, total_parts):
    in_clusters = 0
    in_clusters_zero = 0
    for i in range(len(clusters[0])):
        for j in range(len(clusters[1])):
            if matrix[i][j] == 1 and clusters[0][i] == clusters[1][j]:
                in_clusters += 1
            elif matrix[i][j] == 0 and clusters[0][i] == clusters[1][j]:
                in_clusters_zero += 1
    return in_clusters / (total_parts + in_clusters_zero)


def shaking_random(clusters, matrix, total_parts):
    local_optimal = optimal = calculate_clusters(clusters, matrix, total_parts)
    num_of_clusters = len(set(custers[0]))
    max_clusters = min(len(clusters[0]), len(clusters[1]))
    repeats_to_do = 5
    repeats_left = 0
    new_solution = best_solution = 0
    prev_optimal = 1
    while local_optimal >= optimal and repeats_left < repeats_to_do:
        if num_of_clusters > 2 and num_of_clusters < max_clusters:
            what_to_do = random()
        elif num_of_clusters > 2:
            what_to_do = 1
        else:
            what_to_do = 0
        if what_to_do:
            first = randint(0, num_of_clusters - 1)
            new_solution = divide_clusters(clusters, first, num_of_clusters - 1)
        else:
            last = first = randint(0, num_of_clusters - 1)
            while last == first:
                last = randint(0, num_of_clusters - 1)
            new_solution = combine_clusters(clusters, first, last)
        num_of_clusters = len(set(custers[0]))
        local_optimal = calculate_clusters(new_solution, matrix, total_parts)
        if local_optimal > prev_optimal:
            best_solution = new_solution
        prev_optimal = local_optimal
        repeats_left += 1
    return best_solution


def shaking_with_local(clusters, matrix, total_parts):
    local_optimal = optimal = calculate_clusters(clusters, matrix, total_parts)
    new_solution = best_solution = 0
    prev_optimal = 1
    num_of_clusters = len(set(clusters[0]))
    for i in range(num_of_clusters):
        new_solution = divide_clusters(clusters, i, num_of_clusters - 1)
        local_optimal = calculate_clusters(new_solution, matrix, total_parts)
        if local_optimal > prev_optimal:
            best_solution = new_solution
            print("Best", best_solution)
            print("Len best", local_optimal)
        prev_optimal = local_optimal
        print("New", new_solution)
        print("Len new", local_optimal)
    for i in range(num_of_clusters - 2):
        for j in range(i + 1, num_of_clusters - 1):
            new_solution = combine_clusters(clusters, i, j)
            local_optimal = calculate_clusters(new_solution, matrix, total_parts)
            if local_optimal > prev_optimal:
                best_solution = new_solution
            print("Best", best_solution)
            print("Len best", local_optimal)
        prev_optimal = local_optimal
        print("New", new_solution)
        print("Len new", local_optimal)
    return best_solution


def shaking(clusters, matrix, total_parts):
    local_optimal = optimal = calculate_clusters(clusters, matrix, total_parts)
    new_solution = best_solution = 0
    num_of_clusters = len(set(clusters[0]))
    for i in range(num_of_clusters):
        new_solution = divide_clusters(clusters, i, num_of_clusters - 1)
        local_optimal = calculate_clusters(new_solution, matrix, total_parts)
        if local_optimal > optimal:
            best_solution = new_solution
            print("Best", best_solution)
            print("Len best", local_optimal)
        print("New", new_solution)
        print("Len new", local_optimal)
    for i in range(num_of_clusters - 2):
        for j in range(i + 1, num_of_clusters - 1):
            new_solution = combine_clusters(clusters, i, j)
            local_optimal = calculate_clusters(new_solution, matrix, total_parts)
            if local_optimal > optimal:
                best_solution = new_solution
                print("Best", best_solution)
                print("Len best", local_optimal)
        print("New", new_solution)
        print("Len new", local_optimal)
        print(new_solution)
    if best_solution:
        return best_solution
    else:
        return clusters


def divide_clusters(clusters, first, last):
    new_solution = list()
    new_solution.append([i for i in clusters[0]])
    new_solution.append([i for i in clusters[1]])
    for i in range(len(clusters[0])):
        if new_solution[0][i] == first:
            if random.randint(0, 1):
                new_solution[0][i] = last + 1
    for i in range(len(clusters[1])):
        if new_solution[1][i] == first:
            if random.randint(0, 1):
                new_solution[1][i] = last + 1
    return new_solution


def combine_clusters(clusters, first, last):
    new_solution = list()
    new_solution.append([i for i in clusters[0]])
    new_solution.append([i for i in clusters[1]])
    for i in range(len(clusters[0])):
        if new_solution[0][i] == last:
            new_solution[0][i] = first
        elif new_solution[0][i] > last:
            new_solution[0][i] -= 1
    for i in range(len(clusters[1])):
        if new_solution[1][i] == last:
            new_solution[1][i] = first
        elif new_solution[1][i] > last:
            new_solution[1][i] -= 1
    return new_solution


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


def change(solution, matrix, total_parts, mod):
    optimal = calculate_clusters(solution, matrix, total_parts)
    for i in range(len(solution[mod])):
        for j in  range(len(set(solution[mod]))):
            if (solution[mod][i] != j):
                new_solution = copy.deepcopy(solution)
                new_solution[mod][i] = j
                new_optimal = calculate_clusters(new_solution, matrix, total_parts)
                if (optimal < new_optimal):
                    solution = copy.deepcopy(new_solution)
                    optimal = new_optimal
    return solution

def change_machine_cluster(solution, matrix, total_parts):
    return change(solution, matrix, total_parts, 0)


def change_parts_cluster(solution, matrix, total_parts):
    return change(solution, matrix, total_parts, 1)


def GDNS(clusters, matrix, total_parts):
    shaking_structures = [shaking, shaking_with_local]
    neighdorhood_structure = [change_machine_cluster, change_parts_cluster]
    final_solution = greedy_algorithm_vns(clusters, matrix)
    k = 0
    while k != len(shaking_structures):
        solution = shaking_structures[k](final_solution, matrix, total_parts)
        l = 0
        print("In GVNS", solution)
        print("Len initial", calculate_clusters(solution, matrix, total_parts))
        while l != len(neighdorhood_structure):
            new_solution = neighdorhood_structure[l](solution, matrix, total_parts)
            print("In GVNS new", new_solution)
            print("Len initial new", calculate_clusters(new_solution, matrix, total_parts))
            if (calculate_clusters(solution, matrix, total_parts) <
                calculate_clusters(new_solution, matrix, total_parts)):
                solution = copy.deepcopy(new_solution)
                l = 1
            else:
                l += 1
        if (calculate_clusters(solution, matrix, total_parts) >
            calculate_clusters(final_solution, matrix, total_parts)):
            final_solution = copy.deepcopy(solution)
            print("Final", final_solution)
            print("Len final", calculate_clusters(final_solution, matrix, total_parts))
            k = 1
        else:
            k += 1
    return final_solution


if __name__ == '__main__':
    quantity = input()
    quantity = [int(i) for i in quantity.split(' ')]
    matrix, total_parts = convert(quantity[0], quantity[1])
    for i in matrix:
        print(i)
    print("-------------------------------------------------")
    clusters = list()
    clusters.append([0 for i in range(quantity[0])])
    clusters.append([0 for i in range(quantity[1])])
    print(clusters) # 1st line - machines, 2nd line - parts
    clusters = greedy_algorithm_vns(clusters, matrix)
    print("-------------------------------------------------")
    print(clusters)
    print(calculate_clusters(clusters, matrix, total_parts))
    print(GDNS(clusters, matrix, total_parts))
