class LongPressedName:
    def isLongPressed(self, name: str, typed: str) -> bool:
        nPtr = 0;
        tPtr = 0;
        if name==typed:
            return True;
        if len(name) > len(typed):
            return False;
        while True:
            if nPtr == len(name) and tPtr < len(typed):
                return False;
            if nPtr < len(name) and tPtr == len(typed):
                return False;

            if name[nPtr] != typed[tPtr]:
                if tPtr > 0:
                    while tPtr < len(typed) and typed[tPtr] == typed[tPtr-1]:
                        tPtr += 1;
                    if tPtr == len(typed) and nPtr < len(name):
                        return False;
                if name[nPtr] != typed[tPtr]:
                    return False;
            nPtr += 1;
            tPtr += 1;
            if nPtr == len(name):
                while tPtr < len(typed):
                    if typed[tPtr] != typed[tPtr-1]:
                        return False;
                    tPtr += 1;
                break;
        return True;


sol = LongPressedName();

print(sol.isLongPressed("alex", "aaleex"));     #True
print(sol.isLongPressed("alex", "aalee"));      #False
print(sol.isLongPressed("alex", "aaleef"));     #False
print(sol.isLongPressed("saeed","ssaaedd"));    #False
print(sol.isLongPressed("pyplrz","ppyypllr"));  #False
