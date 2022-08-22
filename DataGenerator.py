import pandas as pd

if __name__ == '__main__':
    datas = []
    for i in range(200):
        datas.append(dict(inputs=i, outputs=i*2))
    file = pd.DataFrame(datas, columns=["inputs", "outputs"])
    file.to_csv("./test2.csv", index=False)