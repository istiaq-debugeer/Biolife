# from django.shortcuts import render,redirect,get_object_or_404
#
# from task1.models import Products
# from django.views.generic import TemplateView,View
#
# from cart.carts import Cart
#
# class AddToCart(View):
#      def post(self,*args,**kwargs):
#          product_id=kwargs.get('product_id')
#          product=Products.objects.get(id=product_id)
#          cart=Cart(self.request)
#          cart.update(product.id,1)
#
#          context={
#                'producct':product,
#          }
#          return render(request,'pages/shopping-cart.html',context=context)
#
#
#
