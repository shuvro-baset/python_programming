# ====================== A =======================

# def find_max_difference(n):
#     number_of_digits = list(str(n))
#
#     min_permutation = int("".join(sorted(number_of_digits)))
#     max_permutation = int("".join(sorted(number_of_digits, reverse=True)))
#
#     return max_permutation - min_permutation
#
#
# n = int(input().strip())
# print(find_max_difference(n))
#


# =================== F ==============================
# from collections import Counter

#
# def min_letters_to_transform(s, t):
#     s_count = Counter(s)
#     t_count = Counter(t)
#
#     additional_letters_needed = 0
#
#     for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         required = t_count[char] if char in t_count else 0
#         current = s_count[char] if char in s_count else 0
#
#         if required > current:
#             if char == 'X':
#                 additional_letters_needed += 2 * (required - current)
#             elif char == 'B':
#                 additional_letters_needed += 2 * (required - current)
#             else:
#                 additional_letters_needed += (required - current)
#
#     return additional_letters_needed
#
#
# s = input().strip()
# t = input().strip()
#
# print(min_letters_to_transform(s, t))


# ============================= E ==========================
# def probability_last_cable(n, m):
#     if m == 0:
#         return 1.0  # If no cables are inserted randomly, cable n definitely goes to port n
#     elif m == n:
#         return 1.0 / n  # If all cables are inserted randomly, each port is equally likely
#
#     # Calculate probability that the nth cable ends up in the nth port
#     # Probability that the nth port is not occupied by any of the first m cables
#     probability_nth_port_free = (n - 1) / n
#
#     # Recursively calculate the probability for the remaining cables and ports
#     for i in range(m + 1, n):
#         probability_nth_port_free *= (n - i) / (n - i + 1)
#
#     return probability_nth_port_free
#
#
# # Read input values
# n, m = map(int, input().strip().split())
#
# # Calculate the probability
# result = probability_last_cable(n, m)
#
# # Print the result
# print(f"{result:.6f}")


# ================= D =====================
# n = int(input().strip())
#
# pepperoni_count = 0
#
# for _ in range(n):
#     row = input().strip()
#     pepperoni_count += row.count('P') + row.count('p')
#
# print(pepperoni_count)


# ================ C ====================
def assign_command_chain(N, a):
    from heapq import heappush, heappop

    # Create a max-heap for nodes based on their ai values
    max_heap = []
    for i in range(N):
        heappush(max_heap, (-a[i], i))

    # List to store edges
    edges = []

    # List to keep track of available nodes that can be controlled
    available = []

    while max_heap:
        power, node = heappop(max_heap)
        power = -power  # Convert back to positive

        # Self power (each node has power over itself)
        required_power = power - 1  # Because it already has power over itself

        if required_power == 0:
            continue

        while required_power > 0:
            if not available:
                return -1
            connect_to = available.pop()
            edges.append((node + 1, connect_to + 1))
            required_power -= 1

        # Current node can now be controlled by others
        available.append(node)

    if len(edges) > 10 ** 6:
        return -1

    return edges


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    a = list(map(int, data[1:N + 1]))

    result = assign_command_chain(N, a)
    if result == -1:
        print(-1)
    else:
        print(len(result))
        for u, v in result:
            print(u, v)


# For testing purposes, the following block should be uncommented when running locally
if __name__ == "__main__":
    main()
