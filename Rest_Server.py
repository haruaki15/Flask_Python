from flask import Flask,jsonify,request
from multiprocessing import Value,Pool

counter = Value('i',0)
app = Flask(__name__)

array= []
help_message = """
API Usage:
    - GET    /api/list
    - POST   /api/add data={"key": "value"}
    - GET    /api/get/<id>
    - PUT    /api/update/<id> data={"key": "value_to_replace"}
    - DELETE /api/delete/<id>
"""

def id_generator():
    with counter.get_lock():
        counter.Value +=1
        return counter.Value

   
#print counter()
"""
def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(5)
    print (p.map(f,[1,2,3,]))"""
    
    
a=2
a**=10
b=a
print b