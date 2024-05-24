def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from rod {source} to rod {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from rod {source} to rod {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Test the function with 3 disks
num_disks = 3
tower_of_hanoi(num_disks, 'A', 'C', 'B')
