"""
Something like selfbot for https://xello.blue"""

"""
TODO: Add link_discord, fetch"""

#######################################################################################################################x

import requests, json, os

if not os.path.isfile("config.json"):
    open("config.json", "w").write(json.dumps({"token": "your-token"}, indent=4))

config = json.loads(open("config.json", "r").read())

class account:
    def change_username(new, token=config["token"]):
        # changes username
    
        """
        :param new: new username for your account"""

        headers = {
            "Content-Type": "application/json",
            "origin": "https://xello.blue",
            "cookie": f"token={token}"
        }

        data = {
            "new_username": new
        }

        r = requests.post(f"https://xello.blue/api/change-name", headers=headers, json=data)
        return r

    def change_password(old, new, token=config["token"]):
        # changes password

        """
        :param old: old password of account
        :param new: new password for account"""

        headers = {
            "Content-Type": "application/json",
            "origin": "https://xello.blue",
            "cookie": f"token={token}"
        }

        data = {
            "current_password": old,
            "new_password": new
        }

        r = requests.post(f"https://xello.blue/api/change-password", headers=headers, json=data)
        return r
    

    def change_profile(theme, font, bio, show_discord: bool=True, token=config["token"]):
        # changes your profile page (https://xello.blue/u/1)

        """
        :param theme: theme for your profile page `[dark, light, wooden]`
        :param font: font for your profile page `[ubuntu, kanit, rubik]`
        :param bio: text to your about me/bio
        :param show_discord: toggles on/off showing your discord account on profile page"""

        headers = {
            "Content-Type": "application/json",
            "origin": "https://xello.blue",
            "cookie": f"token={token}"
        }

        data = {
            "theme": theme,
            "font": font,
            "bio": bio,
            "showDiscord": show_discord
        }

        r = requests.post(f"https://xello.blue/api/profile", headers=headers, json=data)
        return r

class embed:
    def change(color, title, description, token=config["token"]):
        # changes embed structure

        """
        :param color: hex code of color you want your embed to be `(for ex. FF0000)`
        :param title: title of your embed
        :param description: description of your embed"""

        if not color.startswith("#"):
            color = "#"+color

        headers = {
            "Content-Type": "application/json",
            "origin": "https://xello.blue",
            "cookie": f"token={token}"
        }

        data = {
            "color": f"{color}", 
            "title": f"{title}", 
            "description": f"{description}"
        }

        r = requests.options(f"https://xello.blue/api/embed-config", headers=headers, json=data)
        return r

class uploader:
    def delete(code, token=config["token"]):
        # deletes a image
    
        """
        :param code: code/url of image you want to delete `(for ex. https://xello.blue/usercontent/abcABC1230)`"""

        code = code.replace("https://xello.blue/user-content/", "").replace("https://xello.blue/", "").replace(".png", "")

        headers = {
            "Content-Type": "application/json",
            "origin": "https://xello.blue",
            "cookie": f"token={token}"
        }

        r = requests.delete(f"https://xello.blue/delete-file/{code}", headers=headers)
        return r

    def hide_url(status, token=config["token"]):
        # toggles on/off hide url (bugs)

        """
        :param status: true/false `(not bool)`
        :param token: authorization to xello.blue `(optional)`
        """

        headers = {
            "Content-Type": "application/json",
            "origin": "https://xello.blue",
            "cookie": f"token={token}"
        }

        r = requests.options(f"https://xello.blue/api/hide-url?status={status}", headers=headers)
        return r    

    def reset_api_key(token=config["token"]):
        # resets upload key (you will be logged out on refresh)

        """
        :param: None"""
        
        headers = {
            "Content-Type": "application/json",
            "origin": "https://xello.blue",
            "cookie": f"token={token}"
        }

        r = requests.put(f"https://xello.blue/api/reset-key", headers=headers)
        return r
        
    def download_config(token=config["token"]):
        # downloads sharex config to current directory

        """
        :param: None"""

        headers = {
            "Content-Type": "application/json",
            "origin": "https://xello.blue",
            "cookie": f"token={token}"
        }

        r = requests.get(f"https://xello.blue/api/download-config", headers=headers)
        open(f"config.sxcu", "wb").write(requests.get("https://xello.blue"+r.json()["url"], headers=headers).content)
        return r

account.change_username("helloworld")