from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length = 20)
	age = models.IntegerField()
	password = models.CharField(max_length = 10)
	sex = models.CharField(max_length = 1)

	def __unicode__(self):
		return self.name
		
	# def toJSON(self):
	# 	fields = []
	# 	for field in self._meta.fields:
	# 		fields.append(field.name)

	# 	d = {}
	# 	for attr in fields:
	# 		d[attr] = getattr(self, attr)

	# 	import json
	# 	return json.dumps(d)
