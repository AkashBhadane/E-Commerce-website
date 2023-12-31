from django.db import models
from brand.models import Brand
from django.template.defaultfilters import slugify


class ProductCategory(models.Model):
    """Product Category model class"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='product_categories')
    status = models.BooleanField(default=True)
    show_on_homepage = models.BooleanField(default=False)
    

    def __str__(self):
        """String Representation of object Product Category"""
        return self.name
    
    
    def save(self, *args, **kwargs):
        """overriding"""
        self.slug= slugify(self.name) 
        super(ProductCategory, self).save(*args, **kwargs)

    

    
class ProductVariation(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

    
class ProductTag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """overriding"""
        self.slug= slugify(self.name) 
        super(ProductTag, self).save(*args, **kwargs)

    


class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,related_name="product_category")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    cover_image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=7,decimal_places=2)
    description = models.TextField()
    variation = models.ManyToManyField(ProductVariation, blank=True)
    tags = models.ManyToManyField(ProductTag, blank=True)
    status = models.BooleanField(default=True) 

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """overriding"""
        self.slug= slugify(self.name) 
        super(Product, self).save(*args, **kwargs)

    


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ProductImage")
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return str(self.id)
    


