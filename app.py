from flask import Flask, request, render_template

app = Flask(__name__)

def calculate_carts_and_time_for_goal_boxes(goal_boxes, cartons_per_box, packets_per_carton, packets_per_cart=8000, time_per_cart_hours=2, time_per_cart_minutes=30):
    """
    Calculate the number of carts needed and total time to process to reach a goal number of boxes.
    """
    packets_in_a_box = cartons_per_box * packets_per_carton
    boxes_per_cart = packets_per_cart / packets_in_a_box
    carts_needed = goal_boxes / boxes_per_cart
    total_time_hours = carts_needed * (time_per_cart_hours + time_per_cart_minutes / 60)
    hours = int(total_time_hours)
    minutes = int((total_time_hours - hours) * 60)
    
    return carts_needed, hours, minutes

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        goal_boxes = int(request.form.get('goal_boxes'))
        cartons_per_box = int(request.form.get('cartons_per_box'))
        packets_per_carton = int(request.form.get('packets_per_carton'))
        carts_needed, hours, minutes = calculate_carts_and_time_for_goal_boxes(goal_boxes, cartons_per_box, packets_per_carton)
        return render_template('home.html', carts_needed=carts_needed, hours=hours, minutes=minutes)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

