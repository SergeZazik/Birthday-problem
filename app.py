from flask import Flask, render_template, request

app = Flask(__name__)


def calc_probability(years_: int, number_people_: int, days_range_: int) -> float:
    """
    Returns the probability that at least one pair of people in the room has a date-of-birth difference of no more than a specified date range.
            Parameters:
                    years_ (int): Number of days per year
                    number_people_ (int): Number of people in the room
                    days_range_ (int): Date range
            Returns:
                    result (float): Probability
    """
    calc = number_people_/(years_/days_range_ * 2) * 100
    result = round(calc, 8)
    return result


@app.route('/', methods=['get'])
def main():
    ydays = request.args.get('ydays', type=int, default=365)
    pcnt = request.args.get('pcnt', type=int, default=8)
    drange = request.args.get('drange', type=int, default=7)

    calc = calc_probability(ydays, pcnt, drange)
    result = f'Input data: Number of days per year: {ydays}, Number of people in the room: {pcnt}, ' \
             f'Date range: {drange} - Result: {calc} %'

    return render_template('birthdays.html', message=result)


if __name__ == '__main__':
    app.run()
