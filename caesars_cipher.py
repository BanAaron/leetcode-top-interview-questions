class CaesarsCipher:
    def __init__(self):
        import string

        self.character_set = (
            string.ascii_letters + string.punctuation + string.digits + " "
        )

    def encrypt(self, message: str):
        answer = ""

        for character in message:
            for i, letter in enumerate(self.character_set):
                if character not in self.character_set:
                    raise Exception(f"Unsupported character: {character}")
                elif character == letter and i + 1 == len(self.character_set):
                    answer = answer + self.character_set[0]
                    break
                elif character == letter:
                    answer = answer + self.character_set[i + 1]
                    break
        return answer

    def decrypt(self, message: str):
        answer = ""

        for character in message:
            for i, letter in enumerate(self.character_set):
                if character not in self.character_set:
                    raise Exception(f"Unsupported character: {character}")
                elif character == letter and i == 0:
                    answer = answer + self.character_set[len(self.character_set) - 1]
                    break
                elif character == letter:
                    answer = answer + self.character_set[i - 1]
                    break
        return answer


if __name__ == "__main__":
    cc = CaesarsCipher()

    text = "Hello, my name is Aaron"
    text_encrypted = cc.encrypt(text)
    print(text_encrypted)

    text_decrypted = cc.decrypt(text_encrypted)
    print(text_decrypted)
