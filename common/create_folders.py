import os, sys

def create_folders(items):
    '''
    create folders to download images in your local system.
    input: list of item objects
    output: None 
    '''
    try: 
        print('Starting to create folders...')
        parent_directory = 'Images'
        os.mkdir(parent_directory)
        
        for i in range(len(items)):
            item_directory = f'{parent_directory}/{items[i].get_product_code()}'
            thumbnail_directory = f'{item_directory}/thumbnail_image'
            details_directory = f'{item_directory}/detail_images'

            os.mkdir(item_directory)
            os.makedirs(thumbnail_directory)
            os.makedirs(details_directory)
        print('Completed to create folders')

    except FileExistsError:
        print('Cannot create existing folder.\nDelete "Images" folder, and try again.')
        sys.exit(1)