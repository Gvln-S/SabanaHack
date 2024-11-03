from dataLoader.excel_loader import excelData
from wordBank.findings import findings


findings()
excelData()
palabra = "nodulo"
palabra2= "si"

findings_instance=findings()
if palabra in findings_instance.findings_list and palabra2 in findings_instance.findings_yesorno:
    print("si existe esta palbra")
else:
    print("no se encuentra esta palabra ")


