import numpy as np
from datetime import date


config = {
  "CK": {
    "connect": {
      "host": "localhost"
    },
    "ck_setting": {
      "max_threads": 2
    }
  }
}

# last node is churn

trans_matrix = np.array([[0.1, 0.5, 0.1, 0, 0.3],
                         [0, 0.2, 0.4, 0.1, 0.3],
                         [0, 0.1, 0.1, 0.3, 0.5],
                         [0, 0,   0,   1,   0],
                         [0, 0,   0,   0,   1]])

nodes = ['one', 'two', 'three', 'four', 'churn']
start_date = date(2022, 5, 1)
end_date = date(2022, 5, 30)
