# from django.conf import settings
# from task1.models import Products
#
#
# class Cart(object):
#     def __init__(self,request) ->None:
#         self.session=request.session
#         self.cart_id=settings.CART_ID
#         cart=self.session.get(self.cart_id)
#         self.cart=self.session[self.cart_id]=cart if cart else {}
#
#     def update(self,product_id,quantity=1):
#             product=Products.objects.get(id=product_id)
#             self.session[self.cart_id].setdefault(str(product_id),{'quantity':0})
#             updated_quantity=self.session[self.cart_id][str(product_id)]['quantity']+quantity
#             self.session[self.cart_id][str(product_id)]['quantity']=updated_quantity
#
#             if updated_quantity<1:
#                 del self.session[self.cart_id][str(product_id)]
#             self.save()
#
#     def __iter__(self):
#             product=Products.objects.filter(id__in=list(self.cart.keys()))
#             cart=self.cart.copy()
#
#             for item in cart:
#                 product=Products.objects.get(id=item.id)
#                 cart[str(item.id)]['product']={
#                     "id":item.id,
#                     "category":item.category.title ,
#                     "productcategory":item.productcategory,
#                     "productname":item.productname,
#                     "productDiscountprice"  :float(item.productDiscountprice)
#
#                 }
#                 yield cart[str(item.id)]
#
#
#     def save(self):
#         self.session.modified=True
#     def __len__(self):
#         return len(list(self.cart.keys()))
#
