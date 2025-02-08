foods = {

}
foods_sorted = []
while True:
    try:
        food = input("")

        if food == "exit":
            for food_name in foods_sorted:
                food_count = foods[food_name]
                food_caps = food_name.upper()
                print(food_count, food_caps)
            exit()
        if food in foods:
            x = foods.get(food)
            x += 1
            foods.update({food:x})
        else:
            foods.update({food:1})
        foods_sorted = sorted(foods.keys())
    except EOFError:
            for food_name in foods_sorted:
                food_count = foods[food_name]
                food_caps = food_name.upper()
                print(food_count, food_caps)
            exit()
   
