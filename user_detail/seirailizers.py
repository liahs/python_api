from rest_framework import serializers



class SimpleSerializer(serializers.Serializer):
    """"Serializers a name fiels for testimg our APIVIEW"""
    name=serializers.CharField(max_length=10)

    