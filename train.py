import matplotlib.pyplot as plt

def readdata():
    km = []
    price = []
    data = []

    f=open("data.csv", "r")
    if f.mode == 'r':
        f.readline()
        lines = f.readlines()
        for x in lines:
            data = x.split(",")
            km.append(int(data[0]))
            price.append(int(data[1]))
    else:
        print("couldn't read data")
    return(km, price)

def calc_mean(km):
    mean = 0.0
    for x in km:
        mean += x
    return (mean/len(km))

def calc_aVar(km, price, kmMean, priceMean):
    var1 = 0.0
    var3 = 0.0
    x = 0
    
    while (x < len(km)):
        var1 += (km[x] - kmMean) * (price[x] - priceMean)
        x += 1
    for y in km:
        var3 += pow((y - kmMean),2)
    return (var1 / var3)

def calc_bVar(km, price, aVar):
    var1 = price[0] - (aVar * km[0])
    return (var1)

def draw(km, price, data):
    plt.plot(km, price, 'ro')
    plt.plot(data)
    plt.ylabel("Price")
    plt.xlabel("Km")
    plt.show()

def generateData(km, price, aVar, bVar):
    data = []
    x = 0
    while (x <= max(km)):
        data.append(x*aVar+bVar)
        x += 1
    return (data)

def main():
    km, price = readdata()
    kmMean = calc_mean(km)
    priceMean = calc_mean(price)
    aVar = calc_aVar(km, price, kmMean, priceMean)
    bVar = calc_bVar(km, price, aVar)
    data = generateData(km, price, aVar, bVar)
    draw(km, price, data)


if __name__ == "__main__":
    main()