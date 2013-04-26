#cl=class
#fi=filename
class dummy:
    def __init__(self,cl,fi):
        p=open(fi,"w")
        for met in dir(cl):
            if not met.startswith("_"):
                p.write('"%s":"",\n' % met)
if __name__ == "__main__":
    pass
