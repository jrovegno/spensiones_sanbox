import requests
from datetime import datetime

inityear = {'A': 2002, 'B': 2002, 'C': 1981, 'D': 2002, 'E': 2000}

today = datetime.now()
fin = today.year
conf = today.strftime("%Y%m%d")

for tf, ini in inityear.items():
    source = f'https://www.spensiones.cl/apps/valoresCuotaFondo/vcfAFPxls.php?aaaaini={ini}&aaaafin={fin}&tf={tf}&fecconf={conf}'
    r = requests.get(source)
    path = f'vcf{tf}{ini}-{fin}.csv'

    with open(path, 'wb') as out_file:
        out_file.write(r.content)
