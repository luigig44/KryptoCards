#!/usr/bin/python3

import json
import webbrowser
import base64

# test data begins, insert program here
results = [(85, ([1, 2, 3, 9], 13), '((9-1)+(2+3))'),
(48, ([2, 4, 6, 1], 6), '((6/(2+1))+4)'),
(30, ([3, 10, 5, 18], 11), '(((5+18)+10)/3)'),
(25, ([5, 3, 9, 7], 2), '((9+7)/(5+3))'),
(22, ([2, 7, 13, 20], 8), '(((7-13)*2)+20)')
]
# test data ends
url = 'https://luigig44.github.io/KryptoCards/?data='
# url = 'file:///home/luigi/KryptoCards/index.html?data='
webbrowser.open(url+base64.b64encode(json.dumps(results).encode('ascii')).decode('ascii'))
