from django.db import models

# Create your models here.


class Good(models.Model):
    good_name = models.CharField(max_length=128)
    good_price = models.FloatField()
    # related_name是反向引用，如user.goods
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="goods"
    )

    category = models.ForeignKey("GoodCategory", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.good_name}:{self.good_price}"

    class Meta:
        ordering = ["-good_price"]


class GoodCategory(models.Model):
    name = models.CharField(max_length=32)
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="goodCategories"
    )
    # blank=True 用于表单检查
    # null=True 用于写DB
    # https://stackoverflow.com/a/16589154
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
