# pdfmoneky
generate pdf using pdfmonkey online service with python

Simple import pdfmonkey.py to your project and call pdfmonkey function

This function has three inputs.The secret that you must get from your profile on https://pdfmonkey.io 
website

Document template id that you have to copy from template you have made, and finally the payload 
that you have to make according to the input of the template

for example

///////////////////////////////////////////////////////////////////////////////////////

from pdfmonkey import pdfmonkey

payload = "your payload"

pdfmonkey("Bearer bS97_Wrj5dXpxqJlinw","401Aa102-2Q12-4DF3-90H8-8C9v9D6L8745",payload)

                        ↑                                  ↑                      ↑
                   Your Secret                 Your Document Template ID    Your Payload

///////////////////////////////////////////////////////////////////////////////////////