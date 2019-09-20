from rest_framework import serializers
from apis.news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
        extra_kwargs = {
            "title": {"required": False},
            "story": {"required": False},
            "category": {"required": False},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context')
        if context:
            self.request = context.get('request')

    def create(self, validate_data):
        news = News(**validate_data)
        news.reporter = self.request.user
        news.save()
        return news
