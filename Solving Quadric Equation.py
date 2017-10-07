import cmath
a = 1;
b = 2;
c = 3;
d = (b**2)-(4*a*c);
#print(cmath.sqrt(d))
e = (cmath.sqrt(d))
solution1 = (-b+e)/2*a;
#print(solution1)
solution2 = (-b-e)/2*a;
print('Solutions of the above are:' ,(solution1,solution2))
##########making it user friendly#############
#instead of giving the value inside the code, we can ask user to provide the values
a = float(input("Enter the value of a:"))
b = float(input("Enter the value of b:"))
c = float(input("Enter the value of c:"))
d = (b**2)-(4*a*c);
#print(cmath.sqrt(d))
e = (cmath.sqrt(d))
solution1 = (-b+e)/2*a;
#print(solution1)
solution2 = (-b-e)/2*a;
print('Solutions of the above are:' ,(solution1,solution2))
