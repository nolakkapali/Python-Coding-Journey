# Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

# Input
# The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

# Output
# Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.
N=float(input()) #576.73
notes=[100, 50, 20, 10, 5, 2]
coins=[1, 0.50, 0.25, 0.10, 0.05, 0.01]
for i in notes:
    taka=N//i
    N=N%i
    print(f"{int(taka)} nota (s) de R$ {i:.2f}")

for j in coins:
    paisa=N//j
    N=N%j
    print(f"{int(paisa)} moeda (s) de R$ {j}")