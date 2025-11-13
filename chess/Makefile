CC = clang
CFLAGS = -Wall -Wpedantic -Werror -Wextra

all: main

main: main.o
	$(CC) main.o -o main

main.o: main.cpp
	$(CC) $(CFLAGS) -c main.cpp config.h

clean:
	rm -f main *.o

format:
	clang-format -i -style=file *.[ch]
