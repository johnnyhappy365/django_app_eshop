from django.db import models

# Create your models here.


class Good(models.Model):
    good_name = models.CharField(max_length=128)
    good_price = models.FloatField()
    # related_name是反向引用，如user.goods
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="goods"
    )

    def __str__(self):
        return f"{self.good_name}:{self.good_price}"

    class Meta:
        ordering = ["-good_price"]
