#exception handling function
def exception_handling(st, nd, op):
    #only digits exception    
    try: int(st)
    except: return "Error: Numbers must only contain digits."
    try: int(nd)
    except: return "Error: Numbers must only contain digits."

    #more than 4 digits exception
    if len(st)>4 or len(nd)>4:
        return "Error: Numbers cannot be more than four digits."
    
    #operator exeption
    if op!='-' and op!='+': 
        return "Error: Operator must be '+' or '-'."

def arithmetic_arranger(problems, solve=False):
    line1=line2=line3=line4=''
    side_space = ' ' * 4
    
    #too many problems exception
    if len(problems) > 5:
        return "Error: Too many problems."
    
    #split problems to get variables    
    for pr in problems:
        pieces=pr.split()
        st=pieces[0]
        op=pieces[1]
        nd=pieces[2]
                    
        exp = exception_handling(st, nd, op)
        if exp != None:
            return exp
        
        space = max(len(st), len(nd))
        ist=int(st)
        ind=int(nd)
        
        #execute results and add them to empty list    
        if op=='+':
            res=ist+ind
        else:
            res=ist-ind
        sres=str(res)
          
        #arrange and print problems
        line1 += st.rjust(space + 2)+side_space
        line2 += op + ' ' + nd.rjust(space)+side_space
        line3 += '-' * (space + 2)+side_space
        line4 += sres.rjust(space + 2)+side_space
    
    if solve==True:
        return line1[:-4] + '\n' + line2[:-4] + '\n' + line3[:-4] + '\n' + line4[:-4]
    else: return line1[:-4] + '\n' + line2[:-4] + '\n' + line3[:-4]

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))