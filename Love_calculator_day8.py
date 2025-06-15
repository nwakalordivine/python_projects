def operation(both, count, stat):
    print(f"{both.upper()} occurs {count} times")
    stat += count
    return stat


def calculate_love_score(name1, name2):
    both_names = (name1 + name2).lower()
    lovee = "love"
    truee = "true"

    love = 0
    for lov in lovee:
        count_love = both_names.count(lov)
        love = operation(lov, count_love, love)
    print(f"Total={love}\n")

    true = 0
    for tru in truee:
        count_true = both_names.count(tru)
        true = operation(tru, count_true, true)
    print(f"Total={true}\n")
    print(f"Love score = {love}{true}")


first_name = input("Enter a name: ")
second_name = input("Enter another: ")
calculate_love_score(name1=first_name, name2=second_name)
