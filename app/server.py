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
        name: str,
    ):
        self.client = ClientMeta(host, verify_ssl=False)
        self.client.login(username, password)

    # HOST
    def host_find(self, search: str):
        return self.client.host_find(search)

    def host_add(
        self,
        host: str,
        description: str,
        ipaddress: str | None = None,
    ):
        kwargs = {
            "a_fqdn": host,
            "o_description": description,
            "o_force": True,
        }

        if ipaddress is not None:
            kwargs["o_ip_address"] = ipaddress

        return self.client.host_add(**kwargs)
    
    # GROUP
    def group_find(self, search: str):
        return self.client.group_find(search)

    def group_add(self, name: str):
        return self.client.group_add(a_cn=name)

    def group_del(self, name: str):
        return self.client.group_del(a_cn=name)

    def group_show(self, name: str):
        return self.client.group_show(a_cn=name)

    def group_add_member(self, name: str, username: str):
        return self.client.group_add_member(
            a_cn=name,
            o_user=username
        )
    def group_remove_member(self, name: str, username: str):
        return self.client.group_remove_member(
            a_cn=name,
            o_user=username
        )
    # SUDO
    def sudorule_find(self, search: str):
        return self.client.sudorule_find(search)

    def sudorule_add(self, name: str):
        return self.client.sudorule_add(a_cn=name)

    def sudorule_del(self, name: str):
        return self.client.sudorule_del(a_cn=name)

    def sudorule_disable(self, name: str):
        return self.client.sudorule_disable(a_cn=name)

    def sudorule_enable(self, name: str):
        return self.client.sudorule_enable(a_cn=name)

    def sudorule_show(self, name: str):
        return self.client.sudorule_show(a_cn=name)

    # USER
    def user_find(self, search: str):
        return self.client.user_find(search)

    def user_add(
        self,
        username: str,
        first_name: str,
        last_name: str,
    ):
        full_name = f"{first_name} {last_name}"

        return self.client.user_add(
            a_uid=username,
            o_givenname=first_name,
            o_sn=last_name,
            o_cn=full_name,
            o_preferredlanguage="EN",
        )

    def user_del(self,username: str):
        return self.client.user_del(a_uid=username)

    def user_disable(self,username: str):
        return self.client.user_disable(a_uid=username)

    def user_enable(self,username: str):
        return self.client.user_enable(a_uid=username)

    # HBAC
    def hbacrule_find(self, search: str):
        return self.client.hbacrule_find(search)

    def hbacrule_add(self,name: str):
        return self.client.hbacrule_add(a_cn=name)

    def hbacrule_del(self,name: str,):
        return self.client.hbacrule_del(a_cn=name)

    def hbacrule_disable(self,name: str):
        return self.client.hbacrule_disable(a_cn=name)

    def hbacrule_enable(self, name: str):
        return self.client.hbacrule_enable(self, a_cn=name)

def main():
    ipa = IPAClient(
        host=IPA_HOST,
        username=IPA_USER,
        password=IPA_PASS,
    )

if __name__ == "__main__":
    main()