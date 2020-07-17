

def cat():
    cat_list = [
        ('electronics', 'Electronics'),
        ('books', 'Books'),
        ('appliances', 'Appliances'),
        ('baby', 'Baby'),
        ('beauty', 'Beauty'),
        ('car', 'Car & Bikes'),
        ('clothing', 'Clothings & Accessories'),
        ('collectibles', 'Collectibles'),
        ('computer', 'Computer & Accessories'),
        ('furniture', 'Furniture')
    ]
    cat_list.sort(key=lambda x: x[0])
    return cat_list


def sub_cat():
    subcat_list = [
        ('tv', 'TV'),
        ('audio', 'Audio Devices'),
        ('mobile', 'Mobile'),
        ('hindinovel', 'Hindi Novel'),
        ('engnovel', 'English Novel'),
        ('programming', 'Programming'),
        ('kitchen', 'Kitchen Appliances'),
        ('cooling', 'Cooling Applinces'),
        ('home', 'Home Appliances'),
        ('babyclothing', 'Baby Clothings'),
        ('babycare', 'Baby Care'),
        ('babytoys', 'Activity & toys'),
        ('makeup', 'Makup'),
        ('skincare', 'Skin Care'),
        ('haircare', 'Hair Care'),
        ('carparts', 'Car Parts & Accessories'),
        ('bikeparts', 'Bike Parts & Accessories'),
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids'),
        ('sportsc', 'Sports Collectibles'),
        ('entertainmentc', 'Entertainment Collectibles'),
        ('desktop', 'Desktops'),
        ('laptop', 'Laptops'),
        ('computerparts', 'Computer Parts & Accessories'),
        ('office', 'Office Furniture'),
        ('home', 'Home Furniture'),
    ]
    subcat_list.sort(key=lambda x: x[0])
    return subcat_list
