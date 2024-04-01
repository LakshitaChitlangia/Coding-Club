class Device:
  def __init__(self, brand, model, price):
    self.brand = brand
    self.model = model
    self.price = price

  def describe_device(self):
    print(self.brand, self.model, self.price)


class Phone(Device):
  def __init__(self, brand, model, price, screen_size, camera_megapixels):
    super().__init__(brand, model, price)
    self.screen_size = screen_size
    self.camera_megapixels = camera_megapixels

  def describe_phone(self, name):
    super().describe_device()
    print(self.screen_size, self.camera_megapixels)
    print(name)

phone = Phone("Apple", "iPhone 15", "$100", "6.2 inches", "20 camera_megapixels")
phone.describe_phone("My Phone")
