from rest_framework import serializers


class PollsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    options = serializers.CharField(max_length=100)


class CategoriesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class ModeratorsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=100)


class ServiceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=100)
    approved_by = serializers.IntegerField()


class AppealAnswerSerializer(serializers.Serializer):
    appeal_id = serializers.IntegerField()
    text = serializers.CharField()
    score = serializers.IntegerField()
    to_user_id = serializers.IntegerField()
    from_service_id = serializers.IntegerField()
    date_create = serializers.DateField(read_only=True)
    date_update = serializers.DateField(read_only=True)


class AddressServiceSerializer(serializers.Serializer):
    category_id = serializers.IntegerField()
    service_id = serializers.IntegerField()


class AppealSerializer(serializers.Serializer):
    text = serializers.CharField
    author_id = serializers.IntegerField()
    address_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField()
    email = serializers.EmailField(max_length=255)
    approved_by = serializers.IntegerField()
    date_create = serializers.DateField()
    date_update = serializers.DateField()
    status = serializers.IntegerField()


class UsersSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=100)
    rating = serializers.FloatField()


class CommentsSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    text = serializers.CharField
    post_id = serializers.IntegerField()
    date_create = serializers.DateField(read_only=True)
    date_update = serializers.DateField(read_only=True)


class PostsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    text = serializers.CharField()
    author_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    picture = serializers.ImageField()
    poll_id = serializers.IntegerField()
    date_create = serializers.DateField(auto_now_add=True)
    date_update = serializers.DateField(auto_now=True)
    approved_by = serializers.IntegerField()
