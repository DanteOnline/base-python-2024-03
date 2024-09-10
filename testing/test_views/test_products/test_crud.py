from views.products.crud import ProductsStorage


class TestProductsStorage:

    def test_get_empty(self):
        storage = ProductsStorage()
        assert storage.get() == []
