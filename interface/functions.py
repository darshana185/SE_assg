def validate(f):
    
    file = open(f.name,"r")
    contents = file.read().split('\n')
    results = open("ans.txt", "w")
    contents.append(">")
    #print(contents)
    map = {
        "ttt":"f",
        "ttc":"f",
        "tta":"l",
        "ttg":"l",
        "ctt":"l",
        "ctc":"l",
        "cta":"l",
        "ctg":"l",
        "att":"i",
        "atc":"i",
        "ata":"i",
        "atg":"m",
        "gtt":"v",
        "gtc":"v",
        "gta":"v",
        "gtc":"v",
        "tct":"s",
        "tca":"s",
        "tcc":"s",
        "tcg":"s",
        "ccc":"p",
        "cct":"p",
        "cca":"p",
        "ccg":"p",
        "acc":"t",
        "acg":"t",
        "aca":"t",
        "act":"t",
        "gcc":"a",
        "gca":"a",
        "gcg":"a",
        "gct":"a",
        "tat":'y',
        "tac":"y",
        "cat": "h",
        "cac": "h",
        "caa": "q",
        "cag": "q",
        "aat":"n",
        "aac":"n",
        "aaa":"k",
        "aag":"k",
        "gat":"d",
        "gac":"d",
        "gaa":"e",
        "gag":"e",
        "tgt":"c",
        "tgc":"c",
        "tgg":"w",
        "cgc":"r",
        "cgg":"r",
        "cgt":"r",
        "cga":"r",
        "ggt":"g",
        "ggg":"g",
        "gga":"g",
        "ggc":"g",
        "agt":"s",
        "agc":"s",
        "aga":"r",
        "agg":"r",   
        
    }
    nuc=""
    final=""
    curtag=""
    nexttag=""
    flag=1

    c1=-1
    c2=-1
    for x in contents:           
        if x[0]=='>':
            curtag = nexttag
            nexttag = x          
            c1=c1+1
        else:
            nuc=nuc+x
            c2=c1
            continue
        
        if c2>=0 and c1!=c2:
            final=final+'\n'+curtag+'\n' 
            flag=1       
            nuc=nuc.lower()            
            n=len(nuc)
            c2=-1
            
            if n%3==0 and n!=0:                
                for i in range(0,n,3):                    
                    key = nuc[i:i+3]
                    if i==0:
                        if key!="atg" and key!="gtg" and key!="ttg":
                            flag=0

                    if i!=n-3 :
                        if key=="taa" or key=="tag" or key=="tga":
                            flag=0

                    if flag==1:
                        if ~(key=="taa" or key=="tag" or key=="tga") and key in map:
                            final = final+map[key].upper()
                            
                    else:
                        print("error1")
                        flag=0
                        break
            else:
                print("error2")
                flag=0
                break
            results.write(final)
            nuc=""
            final=""

                
        if flag==0:
            break
        
    return results



            
            
        

        


                
                
            

            
