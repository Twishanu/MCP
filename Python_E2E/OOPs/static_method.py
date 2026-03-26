class Utils:
    @staticmethod ## decorator to make any method -- static, otherwise object creation is needed
    def token_extracter(text):
        return [item.strip() for item in text.split(" ")]
    
raw = "I am going for a walk"
cleaned_text = Utils.token_extracter(raw)

print(cleaned_text)