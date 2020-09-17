import Class.class_instantiate as init
import common.create_folders as cf
import common.download_images as dw
import common.extract as extract
import common.user_input as ui
import common.move_thumbnails as thumb

excel_file, sheet_name, id_column, html_column, thumbnail_column = ui.get_user_input()

pre_items = extract.excel_data(excel_file, sheet_name, thumbnail_column, html_column, id_column)

processed_items = []

for item in pre_items:
    thumbnail, id_num, links = extract.cell_values(item)
    processed_items.append(init.instantiate(thumbnail, id_num, links))

# cf.create_folders(processed_items)

# dw.download_images(processed_items) 

thumb.move_thumbnails(processed_items)