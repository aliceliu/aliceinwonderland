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
        try:
            text = Text(self.request.POST.get('fname').file.read())
        except:
            text = ''
        newtext = text.PrepareData()
        words = text.all_words
        uniquewords = text.GetUniqueWords()
        my_dict = text.GetWordFreq()
        logging.info(my_dict)
        mostf = text.Freq(my_dict, 'most')
        leastf = text.Freq(my_dict, 'least')
        generate = text.GenerateText(5)
        dlength = text.DistributionLength().items()
      #  dulength = DistributionULength().items()
      #  dfreq = DistributionFreq().items()
        palindrome = text.Palindrome()
        
        template_values={
        "text":text,
        "totalwords": len(words),
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
