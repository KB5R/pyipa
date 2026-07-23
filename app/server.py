import os
import urllib3
from dotenv import load_dotenv
from python_freeipa import ClientMeta

load_dotenv()

IPA_HOST = os.getenv("IPA_HOST")
IPA_USER = os.getenv("IPA_USER")
IPA_PASS = os.getenv("IPA_PASS")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class IPAClient:
    def __init__(
        self,
        host: str,
        username: str,
        password: str,
    ):
        self.client = ClientMeta(host, verify_ssl=False)
        self.client.login(username, password)

    def create_user(
        self,
        username: str,
        first_name: str,
        last_name: str,
    ):
        full_name = f"{first_name} {last_name}"

        return self.client.user_add(
            username,
            first_name,
            last_name,
            full_name,
            o_preferredlanguage="EN",
        )

    def find_user(self, search: str):
        return self.client.user_find(search)


def main():
    ipa = IPAClient(
        host=IPA_HOST,
        username=IPA_USER,
        password=IPA_PASS,
    )

    # user = ipa.create_user(
    #     username="test21w2s32321",
    #     first_name="John",
    #     last_name="Doe",
    # )
    # print(user["summary"])

    result = ipa.find_user("test")
    for user in result["result"]:
        print(user["uid"][0])


if __name__ == "__main__":
    main()