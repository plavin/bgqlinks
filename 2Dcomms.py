import bgqshared as sharedlinks
import shutil
import sys
import ast
import contextlib
import sys

class DummyFile(object):
    def write(self, x): pass

@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = DummyFile()
    yield
    sys.stdout = save_stdout

tot = 0
assign = [0 for i in range(33)]
tups = open("tups.out")
for line in tups.readlines():
    f1 = open("tmp1","w+")
    f2 = open("tmp2","w+")
    if  (tot < 33):
        m = [[0 for x in range(4)] for x in range(4)]
        #read tup from file , assign to b
        b = ast.literal_eval(line)
        for i in range(16):
            m[i/4][i%4] = b[i]
        for i in range(4):
            for j in range(4):
                if m[i][j] == True:
                    f1.write("%s\n" % ((i,j,0,0,0),) )
                else:
                    f2.write("%s\n" % ((i,j,0,0,0),) )
        f1.close()
        f2.close()
        with nostdout():
            sl = sharedlinks.main("tmp1", "tmp2")
        if (assign[sl] == 0):
            assign[sl] = 1
            tot+=1
            print tot
            shutil.copyfile("tmp1","2D/comm0-%d.out" % sl);
            shutil.copyfile("tmp2","2D/comm1-%d.out" % sl);
    else:
        break
    
print assign
