def calculate_spread(currience, basket_price):
    if currience == usd or currience == eur:
        x = 1000

    if currience == cny:
        x = 1

    # Проверка, что в списке есть как минимум три элемента
    if len(basket_price) >= 2:
        if currience != eur:
            # Получаем второй и третий элементы
            values = list(basket_price.values())
            first_element = values[0]
            second_element = values[1]
            third_element = values[2]

            # Извлекаем значения из элементов
            value_first = float(first_element)
            value_second = float(second_element)
            value_third = float(third_element) / x

        else:
            values = list(basket_price.values())
            second_element = values[0]
            third_element = values[1]

            # Извлекаем значения из элементов
            value_second = float(second_element)
            value_third = float(third_element) / x

        # Вычисляем разницу
        difference = "{:.3f}".format(value_third - value_second)
        return difference


