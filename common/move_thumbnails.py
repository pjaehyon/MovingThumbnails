from glob import glob
import os

def move_thumbnails(items):
    '''
    for each item,
    get thumbnail name
    find the picture of that name in a folder 
        if found: then move the picture to created folder into /images/$item/thumbnail
        else: report 
    done
    '''
    thumbnails = []
    failures = []
    successes = []
    success_count = 0

    for folder in glob('Thumbnails/*'):
        path = folder + '/'
    
        for f in glob(path + '*'):
            thumbnails.append(f.split('/')[-1])

        for item in items:
            destination_path = f'Images/{item.get_product_code()}/thumbnail_image/'
            thumbnail_name = item.get_thumbnail()

            if thumbnail_name in thumbnails:
                os.rename(path + thumbnail_name, destination_path + thumbnail_name)
                report_item = create_report_item(item.get_product_code(), thumbnail_name)
                successes.append(report_item)
                success_count += 1
                print(f'Successfully moved {thumbnail_name} to the destination folder.')

            else:
                report_item = create_report_item(item.get_product_code(), thumbnail_name)
                failures.append(report_item)
                print(f'Failed to move thumbnail: {thumbnail_name}')

        if success_count == len(items):
            break

    thumbnail_report(len(items), failures, successes)
    print(f'\nDONE! For more information, open "thumbnail_report.txt" in your folder.\n')

def create_report_item(prod_code, thumb_name):
    report_item = {}

    report_item['product_code'] = prod_code
    report_item['thumbnail_name'] = thumb_name

    return report_item

def thumbnail_report(tot, failures, successes):
    '''
    report result of moving thumbnails with txt file.
    '''
    with open('moving_thumbnail_report.txt', 'w') as f:
        f.write(f'***Moving Thumbnails Report***\nTotal thumbnails to move: {tot}\nSuccessfully moved {len(successes)} thumbnails.\nFailed to move {len(failures)} thumbnails.\n\n')
        if len(successes) != 0:
            f.write('***Success List***\n')
            for log in successes:
                f.write(str(log)[1:-1]+'\n')
        if len(failures) != 0:
            f.write('***Failure List***\n')
            for log in failures:
                f.write(str(log)[1:-1]+'\n')