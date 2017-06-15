from basic import import_csv, build_shop_ui, get_apple_data, get_income_on_row, get_row_data

def loading_test():
    assert type(import_csv("shop.csv")).__name__ == "list"

def test_apples_row():
    data = import_csv("shop.csv")
    apples = get_apple_data(data)
    assert apples[1] == "apples"

def test_income_on_apples():
    data = import_csv("shop.csv")
    apples = get_apple_data(data)
    assert get_income_on_row(apples) == 70

def test_ui():
    data = import_csv("shop.csv")
    res = build_shop_ui(data)
    assert res == "apple:20,banana:5,orange:11,mackerel:2,vodka:99"
