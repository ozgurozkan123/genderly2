from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def genderList():
    list_ = ["Male","Female","Agender","Androgyne","Androgynes","Androgynous","Bigender","Cis","Cis Female","Cis Male","Cis Man","Cis Woman","Cisgender","Cisgender Female","Cisgender Male","Cisgender Man","Cisgender Woman","Female to Male","FTM","Gender Fluid","Gender Nonconforming","Gender Questioning","Gender Variant","Genderqueer","Intersex","Male to Female","MTF","Neither","Neutrois","Non-binary","Other","Pangender","Trans","Trans Female","Trans Male","Trans Man","Trans Person","Trans*Female","Trans*Male","Trans*Man","Trans*Person","Trans*Woman","Transexual","Transexual Female","Transexual Male","Transexual Man","Transexual Person","Transexual Woman","Transgender Female","Transgender Person","Transmasculine","Two-spirit"]
    return json.dumps(list_)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
