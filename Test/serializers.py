from rest_framework import serializers
from .models import Noise, Shorthand, AnswersNoise, AnswersShorthand

class AnswerNoiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswersNoise
        fields = ("audioNoise", "availability","text", "correct")
        
class AnswerShorthandSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswersShorthand
        fields = ("audioShorthand", "availability","text", "correct")

class NoiseSerializer(serializers.ModelSerializer):
    answers_noise = AnswerNoiseSerializer(many=True)
    class Meta:
        model = Noise
        fields = ("pk","audio","text","answers_noise")

class ShorthandSerializer(serializers.ModelSerializer):
    answers_shorthand = AnswerShorthandSerializer(many=True)
    class Meta:
        model = Shorthand
        fields = ("audio","text","answers_shorthand")
        
