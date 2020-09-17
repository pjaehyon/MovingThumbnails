import requests, os

def download_images(items):
    '''
    download images.
    input: list of Item objects
    '''
    total_images = 0
    success_count = 0
    failures =[]

    for i in range(len(items)):
        current_product_code = items[i].get_product_code()
        current_product_links = items[i].get_links()
        download_directory = f'Images/{current_product_code}/detail_images' 

        for j in range(len(current_product_links)):
            total_images += 1
            fail = {}
            response = requests.get(current_product_links[j])
            file_name = current_product_links[j].split('/')[-1]

            if response.status_code == 200:
                with open(f'{download_directory}/{file_name}', 'wb') as f:
                    f.write(response.content)
                success_count += 1
                print(f'Successfully downloaded from {current_product_links[j]}')

            else:
                fail['product_code'] = current_product_code 
                fail['link'] = current_product_links[j]
                failures.append(fail)
                print(f'Failed to download from "{current_product_links[j]}" of item, "{current_product_code}". Status code is {response.status_code}')
    
    report_result(total_images, success_count, failures)
    print(f'\nDONE! For more information, open "report.txt" in your folder.\n')

def report_result(tot, sus, failures):
    '''
    report result of download with txt file.
    '''
    with open('download_report.txt', 'w') as f:
        f.write(f'***Download Report***\nTotal images: {tot}\nSuccessfully downloaded {sus} images.\nFailed to download {len(failures)} images.\n\n')
        if len(failures) != 0:
            f.write('***Failure List***\n')
            for log in failures:
                f.write(str(log)[1:-1]+'\n')