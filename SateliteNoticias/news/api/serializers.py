from rest_framework import serializers
from news.models import Edition, News, Comment
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField
import json
import logging
import six

class NewTagListSerializerField(TagListSerializerField):
    def to_internal_value(self, value):
        logging.debug("Oh hai!")

        if isinstance(value, six.string_types):
            if not value:
                value = "[]"
            try:
                if(type(value) == str):
                    if(value.__contains__('"') == True):
                        value = json.loads(value)
                    else:
                        value = value.split(',')

            except ValueError:
                self.fail('invalid_json')

        if not isinstance(value, list):
            self.fail('not_a_list', input_type=type(value).__name__)

        for s in value:
            if not isinstance(s, six.string_types):
                self.fail('not_a_str')

            self.child.run_validation(s)

        return value
class Newserializer(TaggitSerializer,serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    editions_count = serializers.SerializerMethodField(read_only=True)
    user_has_editioned = serializers.SerializerMethodField(read_only=True)
    tags = NewTagListSerializerField()

    class Meta:
        model = News
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_editions_count(self, instance):
        return instance.editions.count()

    def get_user_has_editioned(self, instance):
        request = self.context.get("request")
        return instance.editions.filter(author=request.user).exists()

class EditionSerializer(TaggitSerializer,serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    user_has_voted = serializers.SerializerMethodField(read_only=True)
    news_slug = serializers.SerializerMethodField(read_only=True)
    tags = NewTagListSerializerField()

    class Meta:
        model = Edition
        exclude =["news", "voters", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_likes_count(self, instance):
        #Modificar para sacar el promedio despues
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

    def get_news_slug(self, instance):
        return instance.news.slug



class CommentSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    news_slug = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        exclude =["news", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_news_slug(self, instance):
        return instance.news.slug