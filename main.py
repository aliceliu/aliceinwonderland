#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import logging
from alice import *

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template=jinja_environment.get_template("home.html")
        template_values = {}
        html = template.render(template_values)
        self.response.out.write(html)
    
    def post(self):
        text = self.request.POST.get('fname').file.read()
        PrepareData(text)
        words = GetAllWords()
        totalwords = len(words)
        uniquewords = GetUniqueWords()
        my_dict = GetWordFreq()
        mostf = Freq(my_dict, 'most')
        leastf = Freq(my_dict, 'least')
        generate = GenerateText(5)
        dlength = DistributionLength().items()
      #  dulength = DistributionULength().items()
      #  dfreq = DistributionFreq().items()
        palindrome = Palindrome()
        
        template_values={
        "text":text,
        "totalwords":totalwords,
        "uniquewords": len(uniquewords),
        "mostf":mostf,
        "leastf":leastf,
        "generate": generate,
        "palindrome": palindrome,
        "dlength": dlength,
       # "dulength": dulength,
      #  "dfreq": dfreq
    
              }
        template = jinja_environment.get_template("home.html")
        html = template.render(template_values)
        self.response.out.write(html)
        

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
