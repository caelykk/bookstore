from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal, ROUND_HALF_UP

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))])
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/images/", blank=True, null=True)
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal("0.00"),
        validators=[MinValueValidator(Decimal("0.00")), MaxValueValidator(Decimal("100.00"))]
    )


    # простая учётная запись наличия
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


    def get_price_after_discount(self) -> Decimal:
        price = self.price  # ожидаем Decimal из DecimalField
        if self.discount == Decimal("0.00"):
            return price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        final = price * (Decimal("1") - (self.discount / Decimal("100")))
        return max(final.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), Decimal("0.00"))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Book(Product):
    circulation = models.PositiveIntegerField(null=True, blank=True)
    volume = models.PositiveSmallIntegerField(null=True, blank=True)
    page_count = models.PositiveIntegerField(null=True, blank=True)
    edition = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta(Product.Meta):
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.name