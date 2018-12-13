import requests
from datetime import datetime

ini = '2002'
fin = '2018'
tf = 'C'
conf = ''
source = 'https://www.spensiones.cl/apps/valoresCuotaFondo/vcfAFPxls.php?aaaaini=2002&aaaafin=2018&tf=B&fecconf=20181210'
r = requests.get(source)

path = 'vcfA2002-2018.csv'

with open(path, 'wb') as out_file:
    out_file.write(r.content)
