from rest_framework import serializers
from watches.models import Product, Order, ProductOrder


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'product_availability', 'price']


class ProductOrderSerializer(serializers.ModelSerializer):
    # product_id = ProductSerializer(read_only=True)

    class Meta:
        model = ProductOrder
        fields = ['units', 'product_id']


class OrderSerializer(serializers.ModelSerializer):
    product_orders = ProductOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'username', 'phone_number', 'address', 'created_at', 'user', 'product_orders', "get_total"]
        read_only_fields = ['user']

    def create(self, validated_data):
        print(validated_data)
        product_orders = validated_data.pop('product_orders')
        order = Order.objects.create(**validated_data)
        print(order.pk)
        for product in product_orders:
            ProductOrder.objects.create(order_id=order, units=product['units'], product_id=product['product_id'])
        return order


# class BucketSerializer(serializers.ModelSerializer):
#     product_id = ProductSerializer()
#
#     class Meta:
#         model = ProductOrder
#         fields = ['id', 'units', 'product_id', 'order_id']
#         read_only_fields = ['order_id']
#
#     def create(self, validated_data):
#         print(validated_data)
#         product_id = validated_data.pop('product_id')
#         product_order = ProductOrder.objects.create(**validated_data)
#         for data in product_id:
#             Product.objects.create(name=data['name'],
#                                    description=data['description'],
#                                    category=data['category'],
#                                    product_availability=data['product_availability'],
#                                    price= data['price'],
#                                    product_orders= product_order
#                                    )
#         return product_order
