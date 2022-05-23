from config import nodes, trans_matrix
from ClickhouseHelper import ClickhouseHelper
from generate_all_paths import populate


def main():
    ck = ClickhouseHelper()
    g = populate(trans_matrix)
    g.print_all_paths(0, len(nodes) - 2)

    for path in g.paths:
        res, total_uid = ck.window_funnel('action', path)
        res = {path[i]: f'{res[i][1] / total_uid * 100} %' for i in range(len(res))}
        print(res)


if __name__ == "__main__":
    main()
