import openpyxl

TheArray = [['No', 'Device_Name', 'Alias', 'Team'], ['1', 'iphonese', 'v-arupra@microsoft.com', 'officelens'], ['2', 'iphone6', 'v-amvutu@microsoft.com', 'wxp'], ['3', 'iphone7', 'v-sajara@microsoft.com', 'kaizala'], ['4', 'iphone8', 'v-chered@microsoft.com', 'visio']]

# # we gonna write the below array to the xl file
# array = ['No', 'Device_Name', 'Alias', 'Team']

def createXL(name):
    filename = name + ".xlsx"
    wb = openpyxl.Workbook()
    wb.save(filename)
    print("Created "+ filename +"!")


# createXL(file)

file = "test123.xlsx"

wb = openpyxl.load_workbook(file)
sheet = wb.active


def XLhorizontalPrinter(array, rowNumber):
    for i, element in enumerate(array):
        sheet.cell(row = rowNumber ,column = i+1).value = element


for i in range(1, len(TheArray) + 1):
    XLhorizontalPrinter(TheArray[i - 1], i)

wb.save(file)
