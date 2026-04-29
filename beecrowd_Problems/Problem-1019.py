# Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

# Input
# The input file contains an integer N.

# Output
# Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.
N=int(input())
h=N//3600
m=(N%3600)//60
s=(N%3600)%60
print(f"{h}:{m}:{s}",end="")