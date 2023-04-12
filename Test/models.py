from django.db import models
import os
from django.utils.deconstruct import deconstructible
from uuid import uuid4
@deconstructible
class PathAndRenameAudio(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            complaint_id = "%s" % (instance.pk,)
            filename = '{}.{}'.format(complaint_id, ext)
        else:
            # set filename as random string
            random_id = "rid_%s" % (uuid4().hex,)
            filename = '{}.{}'.format(random_id, ext)
            # return the whole path to the file
        return os.path.join(self.path, filename)
@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.audio.name:
            complaint_id = "%s" % (instance.audio.name.split("/")[-1].split(".")[0],)
            filename = '{}.{}'.format(complaint_id, ext)
        else:
            # set filename as random string
            random_id = "rid_%s" % (uuid4().hex,)
            filename = '{}.{}'.format(random_id, ext)
            # return the whole path to the file
        return os.path.join(self.path, filename)
path_and_rename_audio = PathAndRenameAudio("noise_audio/")
path_and_rename_csv = PathAndRename("noise_csv/")
# Create your models here.
class Noise(models.Model):
    # id из хеша
    audio = models.FileField(upload_to=path_and_rename_audio)
    #text = models.FileField(upload_to=path_and_rename_csv)
    ## 
    
class Shorthand(models.Model):
    # id из хеша
    audio = models.FileField(upload_to="shorthand_audio/")
    #text = models.FileField(upload_to="shorthand_csv/")
    
# Пустышки - таблица

class AnswersNoise(models.Model):
    audioNoise = models.ForeignKey(Noise, on_delete=models.CASCADE, related_name="answers_noise")
    availability = models.BooleanField()
    text = models.CharField(max_length=255, null=True)
    correct = models.BooleanField(default=False)
    ## пол, возраст, гарнитура, звуковая карта(или пк/ноут)
    
class AnswersShorthand(models.Model):
    audioShorthand = models.ForeignKey(Shorthand, on_delete=models.CASCADE, related_name="answers_shorthand")
    availability = models.BooleanField()
    text = models.CharField(max_length=255, null=True)
    correct = models.BooleanField(default=False)
    
    