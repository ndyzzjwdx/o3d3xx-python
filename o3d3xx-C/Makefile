include ../Makefile.conf

all: test.o 
	chmod 644 test.o
	cp -p readCSV.o ${OBJ_DIR}/

clean:
	rm -f test.o

# test.o: test.cpp ../settings.h
#	${CPP} ${CPPFLAGS} -o test.o -c test.cpp
