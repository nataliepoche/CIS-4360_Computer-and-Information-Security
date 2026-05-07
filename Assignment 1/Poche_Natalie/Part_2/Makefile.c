# Define the compiler
CC = gcc

# Define the target executable name
c_program: c_program.c

# The default rule that runs when you just type 'make'
all: c_program

# Rule to link the program
# It depends on c_program.c; if the .c file changes, this runs again
c_program: c_program.c
	gcc -o c_program c_program.c

# Clean rule to remove the binary
clean:
	rm -f c_program