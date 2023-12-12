from operator import index
import pandas as pd 

dicionario = {

'meses' :    ['janeiro','feveiro','marco','janeiro','feveiro','marco'],
'produtos' : ["uva","maça","pera","uva","maça","pera"],
'valores' :  [150,250,390,150,250,390]
}

df = pd.DataFrame(dicionario) 
print (df)





       
 