#!/usr/bin/python3

import json
import webbrowser

# test data begins, insert program here
results = [(85, ([1, 2, 3, 9], 13), '((9-1)+(2+3))'),
(48, ([2, 4, 6, 1], 6), '((6/(2+1))+4)'),
(30, ([3, 10, 5, 18], 11), '(((5+18)+10)/3)'),
(25, ([5, 3, 9, 7], 2), '((9+7)/(5+3))'),
(22, ([2, 7, 13, 20], 8), '(((7-13)*2)+20)')
]
# test data ends

webbrowser.open('https://luigig44.github.io/KryptoCards/?data='+json.dumps(results))
