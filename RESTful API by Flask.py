#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, jsonify
from flask_restful import Api, Resource
import json 


app = Flask(__name__)
api = Api(app)

with open('results.json') as f:    
    data_list = json.load(f)
    
class Data(Resource):    
    def get(self, floor):        
        json_list = []        
        for data in data_list:            
            if data['總樓層數'] == floor:                
                json_list.append(data)                
        return jsonify(json_list)
            
class DataList(Resource):    
    def get(self):        
        return {'data_list': data_list}
 
api.add_resource(Data, '/floors/<int:floor>')
api.add_resource(DataList, '/floors')

if __name__ == '__main__':    
    app.run(debug = True)

