CC = clang
CFLAGS = -Wall -Wpedantic -Werror -Wextra

all: chess

chess: chess.o
	$(CC) chess.o -o chess

chess.o: chess.cpp
	$(CC) $(CFLAGS) -c chess.cpp config.h

clean:
	rm -f chess *.o

format:
	clang-format -i -style=file *.[ch]
