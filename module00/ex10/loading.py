from time import sleep, time


def ft_progress(lst: list):
    len_lst = len(lst)
    len_bar = 20
    current_time = time()
    for i, elem in enumerate(lst, 1):
        pourcent = int(i * 100 / len_lst)
        bar_fill = int(len_bar * i // len_lst)
        bar = '=' * bar_fill + '>' + ' ' * (len_bar - bar_fill)
        time_left = (time() - current_time) / i * (len_lst - i)
        print("ETA: {:.2f}s [ {: 2d}%][{}] {: 4d}/{} | elapsed time {:.2f}s"
              .format(time_left, pourcent, bar, i,
                      len_lst, time() - current_time), end="\r")
        yield elem


if __name__ == '__main__':
    listy = range(3000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    # print(ret)
