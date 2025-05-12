#created by btonbybton 5/11/25, you are welcome to edit this code however
#Main loop has all the decision information, calls Notes
def main():
    print("1-Derivatives/Rules\n2-Integrals/Rules\n3-Trig Identities\n4-Volume\n5-fund. theorem\n6-Physics")
    input("next page")
    print("7-Taylor/Maclaurin\n8-Euler's Method\n9-Series Convergence/Divergence\n10-Arc Length\n11-Polar\n12-graphing\n13-etc\n0-Before you start")
    choice = int(input())
    notes(choice)

#The big If/Else tree, calls Choice segment of notes
def notes(choice):
    if choice == 1:
        derivative()
    elif choice == 2:
        integrals()
    elif choice == 3:
        trig()
    elif choice == 4:
        volume()
    elif choice == 5:
        fund()
    elif choice == 6:
        physics()
    elif choice == 7:
        taylor()
    elif choice == 8:
        euler()
    elif choice == 9:
        series()
    elif choice == 10:
        arcs()
    elif choice == 11:
        polar()
    elif choice == 12:
        graph()
    elif choice == 13:
        etc()
    elif choice == 0:
        explain()
    else:
        print("ummm try a number 1-12")
        main()

#every function below here is notes
def derivative():
    print("1-Derivatives\n2-Rules\n3-Definition")
    choice = int(input())
    if choice == 1:
        print("x^n = nx^(n-1)\nln(x) = 1/x\nlog_b(x)=1/(xln(b))\ne^x = e^x\nsin(x) = cos(x)\ncos(x) = -sin(x)")
        input("next page")
        print("tan(x) = sec^2(x)\nsec(x) = sec(x) tan(x)\narcsin(x) = 1/(sqrt(1-x^2))\narccos(x) = -1/(sqrt(1-x^2))\narctan(x) = 1/(1+x^2)")
    elif choice == 2:
        print("Product Rule:\nf*g = f'*g + f*g'\nQuotient Rule:\nf/g = (f'*g-f*g')/(g^2)\nChain Rule:\nf(g(x)) = f'(g(x))*g'(x)\nPower Rule:x^n = nx^(n-1)")
    else:
        print("f'(x) = lim_h->0((f(x+h)-f(x))/h)")
        
def integrals():
    print("x^n dx = (x^(n+1))/(n+1) +C\n1/x dx = ln|x|+C\nU-Substitution\nf(g(x))dx let u = g(x)")
    input("next page")
    print("Integration by parts\nu dv = uv - Integral(vdu)\nPartial Fraction\n1/((cx+d)(hx+k)) = A/(cx+d) + B/(hx+k) = (A(hx+k)+B(cx+d))/((cx+d)(hx+k))\nthen solve for A and B\nIntegral(A/(cx+d)) + Integral(B/(hx+k))")
    
def trig():
    print("tan(x) = sin(x)/cos(x)\nsin^2(x)+cos^2(x) = 1")
    
def volume():
    print("Disc\nV = pi*Integral_^b_\\/a(r^2)\nWasher\nV = pi*Integral_^b_\\/a(R^2-r^2)\nShell\nV = 2pi*Integral_^b_\\/a(rh)\nCross Section\nV = Integral_^b_\\/a(A)")
    
def fund():
    print("1st fund. theorem\nd/dx Integral_^g(x)_\\/a(f(t)dt) = f(g(x))*g'(x)\n2nd fund. theorem\nIntegral_^b_\\/a(f(t)dt) = F(b)-F(a) where F'(x) = f(x)")
    
def physics():
    print("v(t) = d/dt(position)\na(t) = d/dt(v(t))\ndisplacement\nIntegral_^a_\\/b(v(t)dt)\nT.D.T.\nIntegral_^a_\\/b(|v(t)|dt)\nspeed = |velocity|\nPolar speed in polar section")
    
def taylor():
    print("1-Special\n2-Taylor/Maclaurin")
    choice = int(input())
    if choice == 1:
        print("e^x = 1 + x + (x^2)/2! + (x^3)/3! + ... + (x^n)/n!\nsin(x) = x - (x^3)/3! + (x^5)/5! - ... + (((-1)^n)*x^(2n+1))/((2n+1)!))")
        print("cos(x) = 1 - (x^2)/2! + (x^4)/4! - ... + (((-1)^n)*x^(2n))/((2n)!))")
    else:
        print("Maclaurin is Taylor at a=0\nf(x) = f(a) + f'(a)(x-a) + (f\"(a)/2!)*(x-a)^2 + ... + ((f^n(a))/n!)*(x-a)^n")
    
def euler():
    print("1-Solver\n2-Table Setup")
    choice = int(input())
    if choice == 1:
        print("Remember, this is a crude and basic calculator\nEnter the dy/dx (example: 'x**2 + 3*x - 5') Only divide, multiply, add, subtract, and exponent(**): ")
        formula = input()
        func = lambda x,y: eval(formula)
        print("Initial x value?")
        x0 = float(input())
        print("Initial y value?")
        y0 = float(input())
        print("Step size?")
        h = float(input())
        print("Number of steps?")
        n = int(input())
        print(esolve(func, x0, y0, h, n))
    else:    
        print("(x,y)|dy/x|delta x|delta y = dy/dx delta x|(x,y)")
    
def esolve(func, x0, y0, h, n):
    #this was kinda hard ngl
    #func:callable, x0:decimal, y0:decimal, h:decimal, n:integer
    x = x0
    y = y0
    results = [(x, y)]
    for i in range(n):
        y = y + h * func(x, y)
        x = x + h
        results.append((x, y))
    return results

def series():
    print("Sigma() is the summation symbol (backwards 3)\nNth term test\ndiv. if limit as n -> inf doesn't equal zero\nGeometric\nSigma(ar^n), |r|<1 conv., |r|>1 div., S = a/(1-r)")
    input("next page")
    print("p-series\nSigma(1/n^p), p>1 = conv., p <= 1 = div.\nAlternating Series\ndecr. terms and limit n-> inf = zero then convergent")
    input("next page")
    print("Integral test\na\\/n = f(x), Sigma(a\\/n) conv. if Integral_^inf_\\/1(f(x)dx) conv. Vice versa is true.\nRatio test\nIf limit n->inf |(a\\/(n+1))/(a\\/n)| < 1 conv., > 1 div. = 1 inconclusive.")
    input("next page")
    print("Limit Comparison\nIf lim n->inf (a\\/n)/(b\\/n) is finite and positive, both series act the same.")
    
def arcs():
    print("Cartesian\nIntegral_^b_\\/a(sqrt(1+(dy/dx)^2)dx)\nParametric\nIntegral_^t2_t\\/1(sqrt((dx/dt)^2+(dy/dt)^2)dt)")
    
def polar():
    print("\"O\" means theta\nPolar Area\n1/2*Integral_^O2_\\/O1((r^2)dO)")
    input("next page")
    print("\nConversion\nr^2=x^2+y^2, x=rcos(O), y=rsin(O), O=arctan(y/x)\nSpeed(polar)\nsqrt((dx/dt)^2+(dy/dt)^2)\nT.D.T.\nSame as above (f(x)), but add Integral_^t2_\\/t1(f(x))dx")
    
def graph():
    print("1st derivative test\nFind critical numbers where f'(x) = 0\nCreate intervals\nTest intervals in f'(x)\nDetermine max/min.")
    input("next page")
    print("Concavity test\nCritical numbers of 2nd derivative\nTest, f\"(x)>0, concave up. f\"(x)<0 concave down")
    
def etc():
    print("1-Rate of Change\n2-Mean Value Theorem\n3-Logistics\n4-etc etc")
    choice = int(input())
    if choice == 1:
        print("Average Rate of Change\n(f(b)-f(a))/(b-a)\nInst. Rate of Change\nf'(c)")
    elif choice == 2:
        print("Part 1\nf'(c) = (f(b)-f(a))/(b-a)\nPart 2\nf(c) = (Integral_ba(f(x)dx))/(b-a)")
    elif choice == 3:
        print("M=Carrying Capacity\ndP/dt = (k/M)*P(M-P)\nP=M/(1+Ce^(-kt))")
    else:
        print("Rolles Theorem\nif f(a) = f(b), then f'(c) = 0\nIntermediate val.\nContinous function [a,b] has every y value between f(a) and f(b)\nPoint Slope Form y-y1=m(x-x1)")
        
def explain():
    print("Some notes are too big to fit into a page, and you can't scroll during input. Because of this, some note pages are broken up. Whenever it says \"next page\" or \"return to main menu\" simply press enter. Answers matter when there isn't any prompt")

print("Skip first menu, then push 0. 2nd+mode to quit. \\/ means subscript. Stay hydrated.")

while True:
    main()
    input("return to main menu")
