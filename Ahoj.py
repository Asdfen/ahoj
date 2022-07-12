divna = "Mišulín"
divny = "Jirka"

cas_bez_Tebe = 4
# čas kdy Tě nemůžu vidět [ve dnech]

if 0 <= cas_bez_Tebe < 1:
    print(divny + " momentálně v přítomnosti " + divna + " a je šťastný")

elif 1 <= cas_bez_Tebe < 2:
    print(divny + " vzpomíná na včerejšek prožitý s " + divna + " a je šťastný")

elif 2 <= cas_bez_Tebe < 3:
    print(divny + " vzpomína na poslední chvíle s " + divna + " a vymýšlí, kdy Ji zase uvidí")

elif 3 <= cas_bez_Tebe < 4:
    print(divny + " už má absťák a musí nutně vidět " + divna + "nebo aspoň vědět, kdy Ji uvidí")

elif 4 <= cas_bez_Tebe < 10:
    print(divny + " se stýská po " + divna + " a vymýšlí kraviny, aby Ji mohl zase vidět")
    print("Kaktus už se začíná ptát na " + divna)

elif 10 <= cas_bez_Tebe < 20:
    print(divny + " začíná blouznit a otáči se na ulici za každou holkou, jelikož v každý vidí " + divna + " ,bohužel mylně")
    print("Kaktus dává " + divny + " poslední varování, aby se urychleně mohl setkat s " + divna)

else:
    print(divny + " sice žije, ale něco mu v životě chybí...")
    print("Ano " + divna + " jsi to Ty!!!")
    print("Kaktus utíka z domova, nechce žít pouze s " + divny + "(je to tyran, který nezalévá)" + " bez " + divna)

#Už mi dochází nápady, jakým způsobem Ti říct, co pro mě znamenáš