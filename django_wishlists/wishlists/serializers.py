from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from wishlists.models import Item, Wishlist
import logging

logger = logging.getLogger('M295_logger')


class ItemSerializer(ModelSerializer):
    """
    Serializer for the Item model. It includes the user field as a read-only field.
    """
    user = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

    def create(self, validated_data):
        """
        Create a new Item object with the user making the request and log the creation.
        :param validated_data: The validated data from the request.
        :return: The created Item object.
        """
        item = Item.objects.create(**validated_data, user=self.context['request'].user)
        logger.info(f'------------------------------------------\n'
                    f'Item created successfully:\n'
                    f'{item.__str__()}'
                    f'\n------------------------------------------')
        return item

    def get_user(self, obj):
        """
        Get the username of the user who created the item. Gets displayed instead of the user's pk.
        :param obj: The Item object.
        :return: The username of the user who created the item.
        """
        return obj.user.username


class WishlistSerializer(ModelSerializer):
    """
    Serializer for the Wishlist model. It includes items being displayed with the ItemSerializer, items_pk to add items
    and the user field as a read-only field.
    """
    items = ItemSerializer(many=True, read_only=True)
    items_pk = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Wishlist
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

    def create(self, validated_data):
        """
        Create a new Wishlist object with the user making the request and log the creation. Use the items_pk attribute
        to add items to the wishlist.
        :param validated_data: The validated data from the request.
        :return: The created Wishlist object.
        """
        items_pk = validated_data.pop('items_pk', [])
        wishlist = Wishlist.objects.create(**validated_data, user=self.context['request'].user)
        for item_pk in items_pk:
            wishlist.items.add(item_pk)
        logger.info(f'------------------------------------------\n'
                    f'Wishlist created successfully:\n'
                    f'{wishlist.__str__()}'
                    f'\n------------------------------------------')
        return wishlist

    def update(self, instance, validated_data):
        """
        When updating a Wishlist object, use the items_pk attribute to replace items in the wishlist.
        :param instance: The Wishlist object being updated.
        :param validated_data: The validated data from the request.
        :return: The updated Wishlist object.
        """
        # check if any items_pk are provided. If so, remove all items from the wishlist and add the new ones.
        items_pk = validated_data.pop('items_pk', [])
        if len(items_pk) > 0:
            instance.items.remove(*instance.items.all())
            for item_pk in items_pk:
                instance.items.add(item_pk)

        # update the other fields of the wishlist if provided.
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

    def get_user(self, obj):
        """
        Get the username of the user who created the wishlist. Gets displayed instead of the user's pk.
        :param obj: The Wishlist object.
        :return: The username of the user who created the wishlist.
        """
        return obj.user.username
