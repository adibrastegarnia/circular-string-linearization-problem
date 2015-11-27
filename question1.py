import sys
from suf_tree import * 

def main():
    # Get String from standard input
    Str = str(sys.argv[1])
    n = len(Str)

    StrStr = Str + Str
    #build suffix tree for SS
    st = SuffixTree(StrStr)
    # create suffix array based on suffix tree
    esa = [x for x in st.sa()]
    #print(esa)
    
    suffixes = []
    StrStr = StrStr + "$"
    # Generate all possible suffixes 
    for i in range(len(StrStr)):
        suffixes.append(StrStr[i:])

    # find lexically smallest string
    for i in range(len(esa)):
       s = suffixes[esa[i]]
       if(len(s) > n):
          smallest = s[0:n]
          break
    for i in range(len(Str)):
        if(Str[-i:]+Str[:-i] == smallest):
            if(i == 0):
              result = 0, n-1
              print ','.join(str(i) for i in result)
            else:
                result = n-i-1, n-i
                print ','.join(str(i) for i in result)
    #print(smallest) 
main()

