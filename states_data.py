import pandas


class States:
    csv = pandas.read_csv("50_states.csv")
    state_list = csv["state"].tolist()
    def __init__(self, answer_state):
        super().__init__()

        self.row = self.csv[self.csv.state == answer_state]


        if not self.row.empty:
            self.x_cor = self.row.iloc[0].x
            self.y_cor = self.row.iloc[0].y
        else:
            self.x_cor = None
            self.y_cor = None

    def is_correct(self):
        if self.row.empty:
            return False
        if self.x_cor is None or self.y_cor is None:
            return False
        return True
