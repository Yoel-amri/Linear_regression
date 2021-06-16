import sys

def predict(milleage):
    f = open("abVariables", "r");
    str = f.readline();
    variables = str.split(',');
    aVar = float(variables[0]);
    bVar = float(variables[1]);
    prediction = aVar * milleage + bVar;
    print(prediction);




def main():
    try:
        milleage = raw_input("Please enter a milleage\n");
        milleage = int(milleage);
        if (milleage <= 0):
            sys.exit("Number should be positive !");
    except:
        sys.exit("Please enter a positive valid number !");
    predict(milleage);
    

if __name__ == "__main__":
    main()