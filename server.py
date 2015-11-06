import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'sndflsnflsdknfklsdnf'

@app.route('/')
def index():
	if not session.get('gold'):
		session['gold'] = 0
	if not session.get('log'):
		session['log'] = ['You started the game!']
  	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
	building = request.form['building']
	if building == 'farm':
		new_gold = random.randrange(10, 21)
		msg = 'Earned %d from the farm!' % new_gold
	elif building == 'cave':
		new_gold = random.randrange(5, 11)
		msg = 'Earned %d from the cave!' % new_gold
	elif building == 'house':
		new_gold = random.randrange(2, 6)
		msg = 'Earned %d from the house!' % new_gold
	elif building == 'casino':
		new_gold = random.randrange(-50, 51)
		if new_gold < 0:
			msg = 'Entered a casino and lost %d :(' % new_gold
		else:
			msg = 'Entered a casino and won %d! :)' % new_gold
	session['gold'] += new_gold
	session['log'].append(msg)
	return redirect('/')

app.run(debug=True)
