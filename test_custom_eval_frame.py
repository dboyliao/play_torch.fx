import custom_eval_frame


def callback():
    print("Hello in callback")


def foo():
    return 1


def main():
    custom_eval_frame.set_eval_frame(callback)
    foo()


if __name__ == "__main__":
    main()
