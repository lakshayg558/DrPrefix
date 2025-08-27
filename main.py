from ruleengine import StringSearch


def main():
    user_input = input("Provide me the Medical Terminology String :")
    return StringSearch(user_input).string_search()



if __name__ == "__main__":
    main()