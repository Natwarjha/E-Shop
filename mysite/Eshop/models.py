from django.db import models

# Create your models here.
class shop(models.Model):
    item_name = models.CharField(max_length=100)
    for_user = models.CharField(
        max_length = 30,
        default ='ShopOwner'
    )
    item_desc = models.CharField(
        max_length=500,
        default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae ratione ipsum tenetur quos expedita distinctio eligendi ea rem eum accusamus sit, dolore possimus tempore, veritatis qui dignissimos officiis fugiat quibusdam."
    )
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length = 500,
        default="https://its.unl.edu/images/services/icons/eShop_Icon-01.png"
    )


    def __str__(self):
        return self.item_name
    