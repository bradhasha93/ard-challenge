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

    def __does_short_url_exist(self, short_url):
        """
        Check to see if short_url exists and print statement if it does not exist
        :param short_url:
        :return: result=True/False
        """
        result = False if self.__links.get(short_url) is None else True
        if not result:
            print(f"`{short_url}` does not exist.")
        return result

    def __get_long_url(self, short_url):
        """
        Retrieve long_url that is mapped to short_url
        :param short_url:
        :return: result=value of long_url
        """
        return self.__links.get(short_url).get("long_url")

    def __increment_clicked_count(self, short_url):
        """
        Increment the clicked count by 1 for the particular short_url
        :param short_url:
        """
        self.__links.get(short_url).update(
            {
                "clicked": self.__get_clicked_count(short_url=short_url) + 1
            }
        )

    def __get_clicked_count(self, short_url):
        """
        Retrieve the total clicks for a particular short_url
        :param short_url:
        :return: result=value of clicked
        """
        return self.__links.get(short_url).get("clicked")

    def __prompt_url(self, main_prompt, additional_prompt):
        """
        Create a prompt to user on command line to ask for URL
        :param main_prompt:
        :param additional_prompt:
        :return: result=user value entered
        """
        return prompt.regex(self.URL_REGEX, main_prompt + (additional_prompt if
                                                           additional_prompt is not None else "") + ": ")

    def add_link(self, short_url, long_url):
        """
        Add a new short_url to long_url mapping to trackk
        :param short_url:
        :param long_url:
        """

        # If short_url is not given by user then generate a short_url that is unique and not in use
        if short_url is None or short_url == "":
            short_url = f"http://tinyurl.com/{uuid.uuid4().hex}"
            while self.__links.get(short_url) is not None:
                short_url = f"http://tinyurl.com/{uuid.uuid4().hex}"

        # Add short_url if it is not already in the map, otherwise print error for user
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
        """
        Delete a short_url mapping
        :param short_url:
        """
        if self.__does_short_url_exist(short_url=short_url):
            print(f"Deleted short_url '{short_url}'")
            del self.__links[short_url]

    def retrieve_long_url(self, short_url):
        """
        Retrieve the long_url associated with a short_url and increment clicked
        :param short_url:
        """
        if self.__does_short_url_exist(short_url=short_url):
            self.__increment_clicked_count(short_url=short_url)
            print(f"Retrieved long_url '{self.__get_long_url(short_url=short_url)}' "
                  f"{self.__get_clicked_count(short_url=short_url)} time(s) using short_url: '{short_url}'")

    def retrieve_short_url_stats(self, short_url):
        """
        Retrieve the stats for a particular short_url
        :param short_url:
        """
        if self.__does_short_url_exist(short_url=short_url):
            print(f"short_url: {short_url}, "
                  f"long_url: {self.__get_long_url(short_url=short_url)}, "
                  f"clicked: {self.__get_clicked_count(short_url=short_url)}")

    def retrieve_all_stats(self):
        """
        Retrieve all stats for all short_urls being tracked
        """
        if self.__links:
            for link in self.__links:
                print(f"short_url: '{link}', "
                      f"long_url: '{self.__get_long_url(short_url=link)}', "
                      f"clicked: '{self.__get_clicked_count(short_url=link)}'")
        else:
            print(f"There are no stats to retrieve.")

    def prompt_short_url(self, additional_prompt=None):
        """
        Prompt user for short_url
        :param additional_prompt:
        :return: result=user value entered
        """
        return self.__prompt_url("Enter short url", additional_prompt)

    def prompt_long_url(self, additional_prompt=None):
        """
        Prompt user for long_url
        :param additional_prompt:
        :return: result=user value entered
        """
        return self.__prompt_url("Enter long url", additional_prompt)
