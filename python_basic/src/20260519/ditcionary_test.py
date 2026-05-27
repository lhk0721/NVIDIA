
pets = [
    {'name' : "구름", "age": 5},
    {'name' : "초코", "age": 3},
    {'name' : "아지", "age": 1},
    {'name' : "호랑이", "age": 1}
]

print('='*80)

# 단순 반복문 이용
print("# 우리 동네 애완 동물들")
for item in pets:
    print(item['name'], str(item['age'])+'살')

print('='*80)

#pandas 이용
import pandas as pd

myData = pd.DataFrame(pets)
print(myData)

print('='*80)

for item in pets:
    print(list(item.values()))