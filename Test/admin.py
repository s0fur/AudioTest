from django.contrib import admin
from .models import Noise, Shorthand, AnswersNoise, AnswersShorthand
# Register your models here.
class AnswerNoiseInLine(admin.StackedInline):
    model = AnswersNoise
    fields = ('availability', 'text')
    extra = 3
class AnswerNoiseAdmin(admin.ModelAdmin):
    inlines = [AnswerNoiseInLine]
    
class AnswerShorthandInLine(admin.StackedInline):
    model = AnswersShorthand
    fields = ('availability', 'text')
    extra = 3
class AnswerShorthandAdmin(admin.ModelAdmin):
    inlines = [AnswerShorthandInLine]

admin.site.register(Noise, AnswerNoiseAdmin)
admin.site.register(Shorthand, AnswerShorthandAdmin)