import random 

soups = ["腌笃鲜", "鲫鱼汤", "삼계탕"]
proteins = ["回锅肉", "곱창", "麻辣香锅"]
veggies = ["大白菜", "冻豆腐", "蓬蒿"]
carbs = ["白米饭", "炸酱面", "불닭볶음면"]
drinks = ["beer", "소주", "奶茶"]
desserts = ["蛋糕", "蛋挞", "香芋派"]

def meal(foodlist): 
  plate = []
  for foodgroup in foodlist: 
    plate.append(foodgroup[random.randint(0,len(foodgroup)-1)])
  return ", ".join(plate)

print ("Today's Menu:", meal([soups, proteins, veggies, carbs, drinks, desserts]))
