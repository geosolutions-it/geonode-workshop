from django.db import models
from geonode.base.models import ResourceBase
from geonode.layers.models import Dataset
from django.db.models.signals import post_save, pre_save
# Create your models here.

class WorkshopModel(models.Model):
    
    def __str__(self) -> str:
        return super().__str__()

    name = models.CharField(max_length=250, null=False)
    data = models.DateField(null=True)
    description = models.TextField(null=False)
    resource = models.ForeignKey(ResourceBase, blank=False, null=False, on_delete=models.CASCADE)



def pre_save_function(instance, *args, **kwargs):
    """
    Declaring the function to be called
    """
    instance.description = f"Let's modify the description!: {instance.description}"


pre_save.connect(pre_save_function, sender=WorkshopModel)

def post_saved_resourcebase(instance, *args, **kwargs):
    """
    Declaring the function to be called when resourcebase is saved
    """
    print(f"We are in the POST SAVE the instance with id: {instance.id}")


post_save.connect(post_saved_resourcebase, sender=Dataset)