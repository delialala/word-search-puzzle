CC = python3

all: run

run:
	$(CC) main.py

clean:
	rm -rf __pycache__
