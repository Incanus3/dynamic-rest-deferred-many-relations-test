from django.db.models import Model, CharField, ForeignKey, PROTECT

class Parent(Model):
  class Meta:
    db_table = 'parents'

  name = CharField(max_length = 32)

class Child(Model):
  class Meta:
    db_table = 'children'

  name   = CharField(max_length = 32)
  parent = ForeignKey(Parent, related_name = 'children', on_delete = PROTECT)
