import sys, os, importlib

def get_user_input():
    excel_source = input('Enter the source of your Excel file in lower case (ex: taobao): ').lower()

    while True:
        excel_file = input('Enter the file name of your Excel file:')
        if excel_file.split('.')[-1] != 'xlsx':
            print('Format must be "xlsx". Convert your file format to xlsx and try again.')
            continue
        else:
            break

    if not os.path.isdir(excel_source):
        sheet = input('Type the name of sheet within excel file.')

        while True:
            id_column = input('Enter the column index to be used as product id in upper case (ex: A equals 0, C equlas 2...): ')
            try:
                id_column = int(id_column)
                break
            except:
                print('Enter integer corresponding column index')
                continue 

        while True:
            html_column = input('Enter the column index to be used including html source (ex: A equals 0, C equlas 2...): ')
            try:
                html_column = int(html_column)
                break
            except:
                print('Enter integer corresponding column index')
                continue 

        while True:
            thumbnail_column = input('Enter the column index to be used including thumbnail file name (ex: A equals 0, C equlas 2...)')
            try:
                thumbnail_column = int(thumbnail_column)
                break
            except:
                print('Enter integer corresponding column index')
                continue 
    else:
        mall_info = importlib.import_module(excel_source + '.info')
        index = mall_info.info
  
        sheet = index['sheet']
        id_column = index['product_code']
        html_column = index['html']
        thumbnail_column = index['thumbnail']

    return excel_file, sheet, id_column, html_column, thumbnail_column