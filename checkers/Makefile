CC = clang
CFLAGS = -Wall -Wpedantic -Werror -Wextra

all: checkers

main: checkers.o
	$(CC) checkers.o -o checkers

checkers.o: checkers.cpp
	$(CC) $(CFLAGS) -c checkers.cpp config.h

clean:
	rm -f checkers *.o

format:
	clang-format -i -style=file *.[ch]
