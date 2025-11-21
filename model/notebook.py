class Notebook:
    def __init__(self, id=None, brand_id=None, model_id=None, ram_id=None, ssd_id=None, price=None, quantity=None):
        self.id = id
        self.brand_id = brand_id
        self.model_id = model_id
        self.ram_id = ram_id
        self.ssd_id = ssd_id
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"<Notebook id={self.id}, brand_id={self.brand_id}, model_id={self.model_id}, ram_id={self.ram_id}, ssd_id={self.ssd_id}, price={self.price}, quantity={self.quantity}>"

