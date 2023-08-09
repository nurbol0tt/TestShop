from rest_framework import serializers

from apps.product.models import Product, Tag


class TagsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ("name",)


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="name", read_only=True
    )
    tags = TagsSerializers(many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "category",
            "price",
            "created_at",
            "tags"
        )
