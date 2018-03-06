class Date:

    date_names = ["January",
                  "February",
                  "March",
                  "April",
                  "May",
                  "June",
                  "July",
                  "August",
                  "September",
                  "October",
                  "November",
                  "December"]
    frames_per_month = 900

    fall_enrollment = 7
    spring_enrollment = 0

    def __init__(self):
        self.current = 0
        self.progress = 0

    def get_month_name(self):
        return Date.date_names[self.current]

    # Returns progress on a scale from 0 to 1. Also returns true if new month
    def increment_time(self):
        new_month = False
        self.progress += 1
        if self.progress > Date.frames_per_month:
            new_month = True
            self.progress = 0
            self.current += 1
            if self.current >= 12:
                self.current = 0
            print(self.get_month_name())
        return self.progress / Date.frames_per_month, new_month;