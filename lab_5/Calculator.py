"""Make Calculater"""
def main():
    """Let's find"""
    n = int(input())

    total_presses = 0

    if n == 1:
        total_presses = len(str(1))
    else:
        i = 1
        while i <= n:
            total_presses += len(str(i)) # นับจำนวนตัวเลข
            if i < n:
                total_presses += 1  # กด +
            i += 1
        total_presses += 1  # กดเท่ากับ

    print(total_presses)

main()
