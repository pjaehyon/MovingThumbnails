import Class.class_definition as clss

def instantiate(thumbnail, product_code, img_links):
    '''
    create Item object
    input: thumbnail, product_code: string, img_links: list of string
    output: an Item object
    '''
    obj = clss.Item(product_code, thumbnail, img_links)
    return obj