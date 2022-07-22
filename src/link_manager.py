import uuid

import prompt


class LinkManager:
    URL_REGEX = r"(\w+://)?"  # protocol (optional)
    r"(\w+\.)?"  # host (optional)
    r"((\w+)\.(\w+))"  # domain
    r"(\.\w+)*"  # top-level domain (optional, can have > 1)
    r"([\w\-\._\~/]*)*(?<!\.)"  # path, params, anchors, etc. (optional))

    def __init__(self):
        self.__links = {}

    def __get_long_url(self, short_url):
        return self.__links.get(short_url).get("long_url")

    def __increment_clicked_count(self, short_url):
        self.__links.get(short_url).update(
            {"clicked": self.__get_clicked_count(short_url=short_url) + 1}
        )

    def __get_clicked_count(self, short_url):
        return self.__links.get(short_url).get("clicked")

    def add_link(self, short_url, long_url):
        if short_url is None or short_url == "":
            short_url = f"http://tinyurl.com/{uuid.uuid4().hex}"
            while self.__links.get(short_url) is not None:
                short_url = f"http://tinyurl.com/{uuid.uuid4().hex}"

        if self.__links.get(short_url) is None:

            if long_url == "":
                print(f"Failed to add short_url: '{short_url}' because long_url cannot be empty.")
            else:
                self.__links[short_url] = {
                    "long_url": long_url,
                    "clicked": 0
                }
                print(f"Added short_url: '{short_url}' mapped to long_url: '{long_url}'")
        else:
            print(f"'{short_url}' is already in use.  "
                  f"You must remove it before it can be re-used.")

    def delete_link(self, short_url):
        if self.__links.get(short_url) is None:
            print(f"`{short_url}` does not exist.")
        else:
            del self.__links[short_url]

    def retrieve_long_url(self, short_url):
        if self.__links.get(short_url) is None:
            print(f"`{short_url}` does not exist.")
        else:
            self.__increment_clicked_count(short_url=short_url)
            print(f"Retrieved long_url '{self.__get_long_url(short_url=short_url)}' "
                  f"{self.__get_clicked_count(short_url=short_url)} time(s) using short_url: `{short_url}'")

    def retrieve_short_url_stats(self, short_url):
        if self.__links.get(short_url) is None:
            print(f"`{short_url}` does not exist.")
        else:
            print(f"short_url: {short_url}, "
                  f"long_url: {self.__get_long_url(short_url=short_url)}, "
                  f"clicked: {self.__get_clicked_count(short_url=short_url)}")

    def retrieve_all_stats(self):
        if self.__links:
            for link in self.__links:
                print(f"short_url: '{link}', "
                      f"long_url: '{self.__get_long_url(short_url=link)}', "
                      f"clicked: '{self.__get_clicked_count(short_url=link)}'")
        else:
            print(f"There are no stats to retrieve.")

    def __prompt_url(self, main_prompt, additional_prompt):
        return prompt.regex(self.URL_REGEX, main_prompt + (additional_prompt if
                                                           additional_prompt is not None else "") + ": ")

    def prompt_short_url(self, additional_prompt=None):
        return self.__prompt_url("Enter short url", additional_prompt)

    def prompt_long_url(self, additional_prompt=None):
        return self.__prompt_url("Enter long url", additional_prompt)
