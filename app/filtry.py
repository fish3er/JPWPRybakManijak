def filter_by_price_range(product, min_price=None, max_price=None):
    """
    Sprawdza czy pojedynczy produkt mieści się w zakresie cenowym

    Args:
        product: Pojedynczy produkt (słownik)
        min_price: Minimalna cena (w zł, opcjonalne)
        max_price: Maksymalna cena (w zł, opcjonalne)

    Returns:
        Produkt jeśli spełnia warunki cenowe, None w przeciwnym przypadku
    """
    try:
        # Konwersja ceny do float (usuwa ' zł' i zamienia ',' na '.')
        price_str = product.get('price', '0')
        price = float(price_str.replace(' zł', '').replace(',', '.'))

        # Sprawdzenie warunków
        min_ok = (min_price is None) or (price >= min_price)
        max_ok = (max_price is None) or (price <= max_price)

        return product if min_ok and max_ok else None
    except (ValueError, AttributeError):
        # Obsługa błędów konwersji ceny
        return None

def filter_by_rating(product, min_rating=None):
    """
    Sprawdza czy pojedynczy produkt spełnia minimalny wymagany rating.

    Args:
        product: Pojedynczy produkt (słownik)
        min_rating: Minimalna ocena produktu (opcjonalne)

    Returns:
        Produkt jeśli spełnia warunek ratingowy, None w przeciwnym przypadku
    """
    try:
        if min_rating is None:
            raise ValueError("Minimalna ocena nie może być None")
        min_rating = float(min_rating)
        rating = product.get('rating', 0)  # Pobierz ocenę produktu, załóżmy, że jest w słowniku
        return product if rating >= min_rating else None
    except AttributeError:
        return None