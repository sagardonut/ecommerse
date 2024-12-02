from django.db import models 
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
import uuid

# Create your models here.

class products(models.Model): 
    type_choices = [
        ('t-shirt','T-shirt'),
        ('full body set', 'full body set'),
        ('pant','Pants'),
        ('outer','Outer'),
        ('hoodie','Hoodie'),  
    ]
    season_choices = [
        ('all season', 'All season'),
         ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('autumn', 'Autumn'),
        ('winter', 'Winter'),
    ]
    wearat_choices = [
         ('casual', 'Casual'),
         ('comic','Comic'),
        ('formal', 'Formal'),
        ('party', 'Party'),
        ('weeding','Weeding'),
        ('sports','Sports'),
        ('others', 'Others')
    ]
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('non_binary', 'Non-Binary'),
        ('Unisex', 'unisex'),
    ]
    catogory_choices = [
        ("all", "All"),
        ("best seller",'Best seller'),
        ("season collection", "season collection"),
        ("to be murdered", "to be murdered"),
        ("new arival","New Arival")
    ]
    name = models.CharField(_("product name"), max_length=250)
    catagory = models.CharField(_("catogries"), max_length=250, choices=catogory_choices, default="ALL")
    price = models.DecimalField(_("Price"), max_digits=6, decimal_places=2)
    img = models.ImageField(_("image field"), upload_to="media/", height_field=None, width_field=None, max_length=None)
    type = models.CharField(_("product type"), max_length=50, choices=type_choices)
    dis = models.TextField(_("product description"),blank=True)
    season = models.CharField(_("product wear season"), max_length=80,choices=season_choices)
    wearat = models.CharField(_("Wear at"), max_length=150,choices=wearat_choices)
    gender = models.CharField(_("Gender specific"), max_length=50, choices=gender_choices)
    slug = models.SlugField(_("slug"),unique=True, blank=True)
   
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products") 
  
    def save(self):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.name)
        super().save()
        
    def __str__(self) -> str:
        return self.name

#generate slug and ensure the slug is unique everytime    
def generate_unique_slug(instance, name_field):
    slug = slugify(name_field)
    model_class = instance.__class__
    while model_class.objects.filter(slug=slug).exists():
        slug = f"{slug}-{uuid.uuid4().hex[:6]}"
    return slug

class cart(models.Model):
    item =models.CharField(max_length=450)
    image =models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    bill_amt =models.DecimalField( max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    
    def __str__(self) -> str:
        return self.bill_amt
