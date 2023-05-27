import re
import requests

# Shell Script by jaykali
# Modified by iampopg
# Email: iampopg@protonmail.com
# github: https://github.com/iampopg
# All_medias: iampopg


class Pmask:
    def __init__(self):
        pass

    def url_checker(self, url):
        if not re.match(r'^https?://', url):
            raise ValueError("Invalid URL. Please use http or https.")

    def process_url(self, phish):
        print("Processing and Modifying Phishing URL")
        print()
        response = requests.get(f"https://is.gd/create.php?format=simple&url={phish}")
        if response.status_code != 200:
            raise ConnectionError("Failed to process the URL.")
        short = response.text.strip()
        shorter = short[8:]
        return shorter

    def mask_domain(self):
        print("\n\033[1;31;42m ### Masking Domain..... ###\033[0m")
        while True:
            try:
                mask = input("Domain to mask the Phishing URL (with http or https), ex: https://google.com, http://anything.org): ")
                self.url_checker(mask)
                return mask
            except ValueError as e:
                print("\033[31m[!] Invalid URL format. Please try again.\033[0m")
            except KeyboardInterrupt:
                print("\nExiting...")
                exit(0)

    def generate_Pmask_url(self, mask, shorter):
        print("\nType social engineering words: (like free-money, best-pubg-tricks)")
        print("\033[31mDon't use space, just use '-' word from your social engineering\033[0m")
        while True:
            try:
                words = input("\033[32m>>>>>\033[0m ")
                if not words:
                    print("\033[31m[!] No words.\033[0m")
                    print("\n Generating Pmask URL...\n")
                    final = f"{mask}@{shorter}"
                    return final
                if " " in words:
                    raise ValueError("Invalid words. Please avoid space.")
                print("\nGenerating Pmask Link...\n")
                final = f"{mask}-{words}@{shorter}"
                return final
            except ValueError as e:
                print("\033[31m[!] Invalid words. Please try again.\033[0m")
            except KeyboardInterrupt:
                print("\nExiting...")
                exit(0)

    def run(self):
        while True:
            try:
                print("Paste Phishing URL(Include http or https): ", end="")
                phish = input()
                self.url_checker(phish)
                shorter = self.process_url(phish)
                mask = self.mask_domain()
                final_url = self.generate_Pmask_url(mask, shorter)
                print(f"Your Pmask url is: \033[32m{final_url}\033[0m")
                exit()
            except (ValueError, ConnectionError) as e:
                print(f"\033[31m[!] Error: {str(e)}\033[0m")
            except KeyboardInterrupt:
                print("\nExiting...")
                exit(0)

if __name__ == "__main__":
    generator = Pmask()
    generator.run()
