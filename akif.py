import math
 
sayi=int(input("bir sayı giriniz"))

try:
    print(math.sqrt(sayi))
except Exception:
    print("negatif olanların karekökü alınmaz")