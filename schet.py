import os
import multiprocessing


def perform_operation(file_path):
    with open(file_path, 'r') as file:
        action = int(file.readline().strip())
        numbers = [float(num) for num in file.readline().split()]

    result = 0

    if action == 1:
        result = sum(numbers)
    elif action == 2:
        result = numbers[0] * numbers[1]
    elif action == 3:
        result = sum(x**2 for x in numbers)

    return result, f"{result} from {file_path}"


def process_files(directory, num_threads):
    files = [f for f in os.listdir(directory) if f.startswith(
        'in_') and f.endswith('.dat')]
    results = []

    with multiprocessing.Pool(processes=num_threads) as pool:
        results = pool.map(perform_operation, [
                           os.path.join(directory, file) for file in files])

    with open(os.path.join(directory, 'out.dat'), 'w') as out_file:
        for result, explanation in results:
            out_file.write(f"{explanation}\n")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <num_threads>")
        sys.exit(1)

    directory_path = sys.argv[1]
    num_threads = int(sys.argv[2])

    process_files(directory_path, num_threads)
