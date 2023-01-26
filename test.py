from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    def get_product_info(self):
        return f'Product id: {self.id}, name: {self.name}, description: {self.description}, price: {self.price}'
    def get_product_info_list(self):
        product_info=[]
        return product_info[self.id,self.name,self.description,self.price]



t_shirt={
    'id':1,
    'name':'Taylor Swift T-shirt',
    'description':'A tshirt collection Lover album',
    'price':28.99
}

#insert new product into collection
product_1 = Product(**t_shirt)
#get product info

product_1.get_product_info_list()

