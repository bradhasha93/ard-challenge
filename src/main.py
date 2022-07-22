import prompt

from src.link_manager import LinkManager

if __name__ == "__main__":
    lm = LinkManager()

    print("#### Link Manager Instructions ####")
    print("# Options")
    print("# 0=Exit")
    print("# 1=Add new short_url mapping to long_url")
    print("# 2=Delete short_url mapping to long_url")
    print("# 3=Retrieve long_url mapping from short_url")
    print("# 4=Retrieve short_url stats")
    print("# 5=Retrieve all stats")
    print("")

    while True:
        option = prompt.regex("[0-5]", "Select an option: ")

        if option.string == "0":
            print("Thank you for using Link Manager.")
            quit(0)

        elif option.string == "1":
            short_url = lm.prompt_short_url()
            long_url = lm.prompt_long_url()
            lm.add_link(short_url=short_url.string, long_url=long_url.string)

        elif option.string == "2":
            short_url = lm.prompt_short_url(additional_prompt=" to delete")
            lm.delete_link(short_url=short_url.string)

        elif option.string == "3":
            short_url = lm.prompt_short_url(additional_prompt=" to retrieve long_url")
            lm.retrieve_long_url(short_url=short_url.string)

        elif option.string == "4":
            short_url = lm.prompt_short_url(additional_prompt=" to retrieve stats")
            lm.retrieve_short_url_stats(short_url=short_url.string)

        elif option.string == "5":
            lm.retrieve_all_stats()

        print("")
