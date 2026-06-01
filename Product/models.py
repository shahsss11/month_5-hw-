from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    @property
    def products_count(self):
        count = 0
        for product in self.products.all():
            count += 1
        return count
    

        

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
    
    @property
    def reviews_list(self):
        return [i.text for i in self.reviews.all()]
    
        
    @property
    def rating(self):
        try:
            stars = [review.stars for review in self.reviews.all()]
            avg_rate = sum(stars) / len(stars)
            return avg_rate
        except:
            return 0
        




class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=((i ,'*' * i)for i in range(1,6)), default=3,)

 
