include Makefile.conf

all:
	make -C o3d3xx-C
	chmod +x script/*

clean:
	make -C o3d3xx-C clean
	rm -f obj/*
	rm -f bin/*


