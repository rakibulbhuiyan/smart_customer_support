class SuggestionService:

    RULES = {
        "refund":"We are sorry for the inconvenience. We can assist with your refund request.",
        "delivery":"We are checking the delivery status.",
        "order":"Could you provide your order number?"
    }

    @classmethod
    def suggest(cls,message):

        text = message.lower()
        for key, value in cls.RULES.items():

            if key in text:
                return value

        return (
            "Thank you for contacting support."
        )