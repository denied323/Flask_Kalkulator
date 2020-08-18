from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def main():
    return render_template("app.html")


@app.route('/send', methods=["POST"])
def send(sum=sum):
    if request.method == "POST":
        cyfra1 = request.form["cyfra1"]
        cyfra2 = request.form["cyfra2"]
        operacja = request.form["operation"]

        if operacja == "dodaj":
            sum = float(cyfra1) + float(cyfra2)
            return render_template("app.html", sum=sum)

        elif operacja == "odejmij":
            sum = float(cyfra1) - float(cyfra2)
            return render_template("app.html", sum=sum)

        elif operacja == "pomnoz":
            sum = float(cyfra1) * float(cyfra2)
            return render_template("app.html", sum=sum)

        elif operacja == "podziel":
            sum = float(cyfra1) / float(cyfra2)
            return render_template("app.html", sum=sum)


        else:
            return render_template("app.html")



@app.route('/send2', methods=["POST"])
def send2(sum2=sum):
    if request.method == "POST":
        cyfra1 = request.form["cyfra1"]
        cyfra2 = request.form["cyfra2"]
        operacja = request.form["operation"]

        if operacja == "procentz":
            sum = float(cyfra1) * float(cyfra2) / 100
            return render_template("app.html", sum2=sum)

        elif operacja == "procentz2":
            sum = float(cyfra1) / float(cyfra2) * (100 / 100)
            return render_template("app.html", sum2=sum)

        else:
            return render_template("app.html")


if __name__ == ' __main__':
    app.debug = True
    app.run()

    