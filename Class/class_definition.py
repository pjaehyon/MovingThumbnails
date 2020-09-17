class Item(object):
    '''
    input - product_code, thumbnail: string
            links: list of image source links
    '''
    def __init__(self, product_code, thumbnail, links):
        self.product_code = product_code
        self.thumbnail = thumbnail
        self.links = links

    def get_product_code(self):
        return self.product_code

    def get_thumbnail(self):
        return self.thumbnail

    def get_links(self):
        return self.links