from flask import Flask,render_template

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/isPrime/<numb>')
def fn(numb):
    isprime = prime(int(numb))
    return render_template('isprime.html', isprime=isprime, N=numb)


@app.route('/<numb>')
def fx(numb):
    return render_template('home.html', N=numb)



def prime(numb):
    if numb > 1:
        for i in range(2, numb):
            if (numb % i) == 0:
                return False
                # not prime
        #prime
        return True
    else:
        return False
        #not prime



app.run()