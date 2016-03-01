RM   = rm -rf
JUNK = tups.out *~ *.pyc

tups.out:
	python tuplegen.py

2D: tups.out bgqshared.py 2Dcomms.py
	mkdir 2D
	python 2Dcomms.py
	rm -rf tmp1 tmp2

clean:
	$(RM) $(JUNK)

clean-all:
	$(RM) $(JUNK) 2D