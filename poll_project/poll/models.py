from django.db import models

# Create your models here.

class Poll(models.Model):
  title = models.CharField(max_length=200, unique=True)
  question = models.TextField()
  active_until = models.DateTimeField(auto_now_add=False)
  status = models.IntegerField(default=0)

class Option(models.Model):
  title = models.CharField(max_length=200, unique=True)
  poll = models.ForeignKey('Poll', on_delete=models.CASCADE)

class Response(models.Model):
  name = models.CharField(max_length=200, unique=False)
  response_time = models.DateTimeField(auto_now_add=True)
  option = models.ForeignKey('Option', on_delete=models.CASCADE)
  poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
