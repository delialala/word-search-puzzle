CC = pyhton3

all: run

run:
	$(CC) main.py

clean:
	rim -rf __pycache__