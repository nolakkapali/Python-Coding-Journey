# Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

# Input
# The input file contains an integer N.

# Output
# Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.
n=int(input())
bank=[100,50,20,10,5,2,1]
for i in bank:
    note=n//i
    n=n%i
    print(f"{note} nota(s) de R$ {i},00")