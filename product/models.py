from django.db import models

# Create your models here.
class Category(models.Model):
    main_class = models.CharField(max_length=25, unique=True)
    sub_class = models.CharField(max_length=25, unique=True)
    shoes_sub = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return '{} : {} : {}'.format(self.main_class, self.sub_class, self.shoes_sub)

class Product(models.Model):
    # 상품번호, 상품명, 상품가격, 카테고리번호, (총재고량), 출시일, 판매량, 썸네일 이미지
    name = models.CharField(max_length=20, unique=True)
    price = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)  # 카테고리에 속한 상품 존재하면 카테고리 삭제 불가
    # total_stock
    release_date = models.DateField()
    sales = models.IntegerField(default=0)   # 판매량 default를 0으로
    thumbnail = models.ImageField(upload_to='product/thumbnail/')

    def __str__(self):
        return '{}'.format(self.name)

class Inventory(models.Model):
    # 상품번호, 사이즈, 재고
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)  # 재고 존재하면 상품 삭제 불가
    size = models.CharField(max_length=10)
    amount = models.IntegerField()

    def __str__(self):
        return '{}: {}'.format(self.product_id, self.size)


class ProductImage(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)  # 상품 삭제하면 이미지도 함께 삭제
    image = models.ImageField(upload_to='product/detailimage/')

    def __str__(self):
        return '{} image'.format(self.product_id)


