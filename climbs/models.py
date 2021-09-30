# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres.fields import ArrayField




class Locations(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    img = models.CharField(max_length=512, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True

    def __str__(self):
        retStr = '{\n'
        retStr+= 'id: ' + str(self.id) + '\n'
        retStr+= 'img: ' + str(self.img) + '\n'
        retStr+= 'width: ' + str(self.width) + '\n'
        retStr+= 'height: ' + str(self.height) + '\n'
        retStr += '}'
        return retStr
 


class Areas(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    img = models.CharField(max_length=512, blank=True, null=True)
    preview = models.CharField(max_length=512, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    coords = ArrayField(models.IntegerField(), blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    location = models.ForeignKey('Locations', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True

    def __str__(self):
        return str(self.id)
 


class Boulders(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    images = ArrayField(models.CharField(max_length=512, blank=True, null=True), blank=True, null=True)
    preview = models.CharField(max_length=512, blank=True, null=True)
    minimap = models.CharField(max_length=512, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    coords = ArrayField(models.IntegerField(), blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


class Climbs(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    grade = models.IntegerField(blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    preview = models.CharField(max_length=512, blank=True, null=True)
    imgidx = models.IntegerField(blank=True, null=True)
    points = ArrayField(models.IntegerField(), blank=True, null=True)
    coords = ArrayField(models.IntegerField(), blank=True, null=True)
    boulder = models.ForeignKey(Boulders, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True


