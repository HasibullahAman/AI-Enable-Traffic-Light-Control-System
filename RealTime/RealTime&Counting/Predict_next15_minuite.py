import pandas as pd
from datetime import datetime
import joblib

class Predict_15_MiniuteLatter:
    def NowTime(self):
        now = datetime.now()
        self.date = now.strftime("%d")
        self.dayC = now.strftime("%A")

        def convert_day_to_numeric(day):
            numeric_value = {
                'Monday': 1,
                'Tuesday': 2,
                'Wednesday': 3,
                'Thursday': 4,
                'Friday': 5,
                'Saturday': 6,
                'Sunday': 7
            }

            return numeric_value.get(day, 'Invalid day')

        # Example usage
        self.day = now.strftime("%A")
        numeric_day = convert_day_to_numeric(self.day)
        return self.date, numeric_day

    def TimeIN_15_minuteFormat(self):
        def round_to_quarter_hour(dt):
            minutes = (dt.minute // 15) * 15
            return dt.replace(minute=minutes, second=0, microsecond=0)

        def ChangeToSec(time):
            time_str = time
            hours, minutes, seconds = map(int, time_str.split(':'))
            total_seconds = hours * 3600 + minutes * 60 + seconds
            return total_seconds

        current_time = datetime.now()
        rounded_time = round_to_quarter_hour(current_time)

        # Generate the next quarter-hour times
        quarter_hour_times = [rounded_time]
        for time in quarter_hour_times:
            Time = time.strftime("%H:%M:%S")
        return ChangeToSec(Time)

    def FindingAMandPM(self):
        def get_am_pm_indicator():
            current_time = datetime.now().strftime("%p")
            if current_time == "AM":
                return 1
            else:
                return 0

        # Get the AM/PM indicator
        am_pm_indicator = get_am_pm_indicator()

        # Return the result
        return am_pm_indicator


instance = Predict_15_MiniuteLatter()
Date, Day = instance.NowTime()
Time = instance.TimeIN_15_minuteFormat()
Am = instance.FindingAMandPM()
data = {
    'Time': [Time],
    'Date': [Date],
    'Day of week': [Day],
    'midday' : [Am]
}
df = pd.DataFrame(data)




class predict:
    # Assuming you have an array called 'data' for prediction
    def predictNext15Minuite():
        model = joblib.load('../../Historical/Model/After15Situation.joblib')
        prediction = model.predict(df)
        return prediction

    situation= predictNext15Minuite()