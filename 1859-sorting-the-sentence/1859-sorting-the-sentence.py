class Solution:
    def sortSentence(self, s: str) -> str:
        result=""
        d=s.split()
        for i in d:
            if(i[len(i)-1]=="1"):
                if len(d)==1:
                    result = result + i[0:-1]
                else:
                    result = result + i[0:-1]+" "
        for i in d:
            if(i[len(i)-1]=="2"):
                if len(d)==2:
                    result = result + i[0:-1]
                else:
                    result = result + i[0:-1]+" "
        for i in d:
            if(i[len(i)-1]=="3"):
                if len(d)==3:
                    result = result + i[0:-1]
                else:
                    result = result + i[0:-1]+" "
        for i in d:
            if(i[len(i)-1]=="4"):
                if len(d)==4:
                    result = result + i[0:-1]
                else:
                    result = result + i[0:-1]+" "
        for i in d:
            if(i[len(i)-1]=="5"):
                if len(d)==5:
                    result = result + i[0:-1]
                else:
                    result = result + i[0:-1]+" "
        for i in d:
            if(i[len(i)-1]=="6"):
                if len(d)==6:
                    result = result + i[0:-1]
                else:
                    result = result + i[0:-1]+" "
        for i in d:
            if(i[len(i)-1]=="7"):
                if len(d)==7:
                    result = result + i[0:-1]
                else:
                    result = result + i[0:-1]+" "
        for i in d:
            if(i[len(i)-1]=="8"):
                if len(d)==8:
                    result = result + i[0:-1]
                else:
                    result = result + i[0:-1]+" "
        for i in d:
            if(i[len(i)-1]=="9"):
                if len(d)==9:
                    result = result + i[0:-1]
                else:
                    result = result + i[0:-1]+" "
        return result
        